import csv
import json
import sqlite3

from Model.Lines import Lines
from Model.Repository.Repository import Repository
from Model.Stations import Stations
from Model.Connections import Connections
import csv

class NetworkRepository:
    def __init__(self):
        self.repository = Repository()
        self.last_row_id = None  # Atribute pentru a stoca lastrowid

    def AddLine(self, line_data):
        number,stations=line_data
        try:
            # Pasul 1: Adăugați linia în tabelul Lines și obțineți ID-ul acesteia
            command_sql_line = f'INSERT INTO Lines (number) VALUES ("{number}")'
            self.repository.CommandSQL(command_sql_line)
            line_id = self.repository.GetLastRowId()

            stationss = [station.strip() for station in stations.split(",")]
            print(stationss)

            # Pasul 2: Adăugați fiecare stație în tabelul Stations dacă nu există și obțineți ID-ul
            for station_name in stationss:
                # Verificați dacă stația există deja
                existing_station = self.repository.GetTable(
                    f'SELECT station_id FROM Stations WHERE name = "{station_name}"')
                if not existing_station:
                    self.add_station(Stations(station_name))
                    station_id = self.repository.GetLastRowId()
                else:
                    station_id = existing_station[0][0]

                # Pasul 3: Asociați stația cu linia în tabelul LineStation
                command_sql_association = f'INSERT INTO LineStation (line_id, station_id) VALUES ({line_id}, {station_id})'
                self.repository.CommandSQL(command_sql_association)

            print("Linia și stațiile au fost adăugate cu succes în baza de date!")
        except Exception as e:
            print(f"Eroare la adăugarea liniei și stațiilor în baza de date: {e}")

    def addConnection(self, connection_data):
        from_station_name, to_station_name, distance = connection_data
        try:
            # Ensure the IDs are integers (if they are strings or other formats, convert or validate them)

            distance = float(distance)  # Ensure distance is a float

            # Build the SQL command directly with string formatting, but only after data type validation
            command_sql = f'INSERT INTO Connections (from_station_id, to_station_id, distance) VALUES ("{from_station_name}", "{to_station_name}", {distance})'
            # Execute the SQL command
            self.repository.CommandSQL(command_sql)
            print("Connection has been successfully added to the database.")
        except ValueError as e:
            print(f"Invalid input data: {e}")
        except Exception as e:
            print(f"Error adding connection to the database: {e}")



    def add_station(self, station):
        command_sql = f'INSERT INTO Stations (name) VALUES ("{station.name}")'
        self.repository.CommandSQL(command_sql)

    def get_all_connections(self):
        # Fetches all connections from the database and returns them
        try:
            return self.repository.GetTable("SELECT from_station_id, to_station_id, distance FROM Connections")
        except Exception as e:
            print(f"Error retrieving connections: {e}")
            return []

    def delete_connection(self,id):

        conn_to_search=self.SearchConnectionByID(id)

        if conn_to_search:
            command_sql = f"DELETE FROM Connections WHERE connection_id={id}"
            return self.repository.CommandSQL(command_sql)
        return False

    def DeleteLine(self, id):
        line_to_find = self.SearchLineByID(id)
        if line_to_find is None:
            print("Line not found")
            return False  # The line does not exist

        # Get all station names associated with the line
        stations = self.repository.GetTable(f"""
            SELECT S.name FROM LineStation LS
            JOIN Stations S ON LS.station_id = S.station_id
            WHERE LS.line_id = {id}
        """)
        if stations:
            station_names = [station_name[0] for station_name in stations]

            # Explicitly delete all connections involving these stations
            for station_name in station_names:
                # Check and delete connections where this station is either the starting point or the ending point
                connections_to_delete = self.repository.GetTable(
                    f"SELECT * FROM Connections WHERE from_station_id = '{station_name}' OR to_station_id = '{station_name}'")
                if connections_to_delete:
                    print(f"Deleting connections for station: {station_name}")
                    delete_connections_sql = f"DELETE FROM Connections WHERE from_station_id = '{station_name}' OR to_station_id = '{station_name}'"
                    self.repository.CommandSQL(delete_connections_sql)

                # Check for incoming connections
                incoming_connections = self.repository.GetTable(
                    f"SELECT * FROM Connections WHERE to_station_name = '{station_name}'")
                if incoming_connections:
                    print(f"Deleting incoming connections for station: {station_name}")
                    delete_incoming_sql = f"DELETE FROM Connections WHERE to_station_name = '{station_name}'"
                    self.repository.CommandSQL(delete_incoming_sql)

            # Delete station associations from LineStation
            self.repository.CommandSQL(f"DELETE FROM LineStation WHERE line_id = {id}")

            # Check and delete any stations not associated with other lines
            for station_name in station_names:
                other_lines = self.repository.GetTable(
                    f"SELECT line_id FROM LineStation LS JOIN Stations S ON LS.station_id = S.station_id WHERE S.name = '{station_name}'")
                if not other_lines:
                    print(f"Deleting station with no other lines: {station_name}")
                    self.repository.CommandSQL(f"DELETE FROM Stations WHERE name = '{station_name}'")

        # Finally, delete the line itself
        self.repository.CommandSQL(f"DELETE FROM Lines WHERE line_id = {id}")
        print("Line and associated stations and connections successfully deleted.")
        return True

    def check_stations_exist(self, from_station_name, to_station_name):
        sql_query_from = f'SELECT station_id FROM Stations WHERE name = "{from_station_name}"'
        sql_query_to = f'SELECT station_id FROM Stations WHERE name = "{to_station_name}"'
        from_station = self.repository.GetTable(sql_query_from)
        to_station = self.repository.GetTable(sql_query_to)

        if not from_station:
            print(f"Station '{from_station_name}' does not exist.")
            return False
        if not to_station:
            print(f"Station '{to_station_name}' does not exist.")
            return False
        return True  # Both stations exist

    def check_connection_exists(self, from_station_name, to_station_name):
        print(from_station_name+"  "+to_station_name)
        # Directly check if a connection between the given station names exists in the Connections table
        sql_query = f'SELECT * FROM Connections WHERE from_station_id = "{from_station_name}" AND to_station_id = "{to_station_name}"'
        existing_connection = self.repository.GetTable(sql_query)

        if existing_connection:
            print("A connection between these stations already exists.")
            return False
        print("de aici eroare")
        return True

    def LinesList(self):
        select_sql = """
            SELECT L.line_id, L.number, GROUP_CONCAT(S.name, ', ') AS stations
            FROM Lines L
            LEFT JOIN LineStation LS ON L.line_id = LS.line_id
            LEFT JOIN Stations S ON LS.station_id = S.station_id
            GROUP BY L.line_id
            ORDER BY L.line_id;
            """
        lines_data = self.repository.GetTable(select_sql)
        lines_list = []
        if lines_data:
            for line_id, number, stations in lines_data:
                line_info = {
                    'line_id': line_id,
                    'number': number,
                    'stations': stations if stations else "No stations"
                }
                lines_list.append(line_info)
        return lines_list


    def SearchLineByID(self, id):
        select_sql = f"SELECT * FROM Lines WHERE line_id = {id}"
        line_data = self.repository.GetTable(select_sql)

        if line_data is None or len(line_data) == 0:
            return None

        line_data = line_data[0]  # Se așteaptă un singur rând
        line = Lines(number=line_data[0],line_id=line_data[1])  # ID-ul liniei
        return line

    def station_by_number(self,number):
        # Find the line ID from the line number
        line_sql = f"SELECT line_id FROM Lines WHERE number = '{number}'"
        line_data = self.repository.GetTable(line_sql)

        if not line_data:
            print("No line found with the specified number.")
            return []

        line_id = line_data[0][0]  # Assuming that line_id is in the first column of the first row

        # Get all station IDs associated with this line ID from LineStation
        station_ids_sql = f"SELECT station_id FROM LineStation WHERE line_id = {line_id}"
        station_ids_data = self.repository.GetTable(station_ids_sql)

        if not station_ids_data:
            print("No stations found for the specified line.")
            return []

        # Retrieve all station names using the station IDs
        station_names = []
        for (station_id,) in station_ids_data:  # Extracting station_id which is assumed to be the first element in each tuple
            station_sql = f"SELECT name FROM Stations WHERE station_id = {station_id}"
            station_name_data = self.repository.GetTable(station_sql)
            if station_name_data:
                station_names.append(station_name_data[0][0])  # Assuming that name is the first column of the first row
        print(station_names)
        return station_names

    def SearchConnectionByID(self, id):
        select_sql = f"SELECT * FROM Connections WHERE connection_id = {id}"
        conn_data = self.repository.GetTable(select_sql)

        if conn_data is None or len(conn_data) == 0:
            return None

        conn_data = conn_data[0]  # Se așteaptă un singur rând
        conn = Connections(connection_id=conn_data[0],from_station_id=conn_data[1],to_station_id=conn_data[2],distance=conn_data[3])

        return conn

    def SearchLineByNumber(self,number):
        select_sql = f"SELECT * FROM Lines WHERE number = {number}"
        line_data=self.repository.GetTable(select_sql)

        if line_data is None or len(line_data)==0:
            return None

        line_data = line_data[0]  # Se așteaptă un singur rând
        line = Lines(number=line_data[1],
                     stations_list=line_data[2].split(','),  # Convertim șirul de stații înapoi într-o listă
                     id=line_data[0])  # ID-ul liniei
        print(f"Line Number: {line.number}, Stations: {', '.join(line.stations_list)}")
        return line

    def DeleteAllLines(self):
        delete_sql = "DELETE FROM Lines"  # Șterge toate înregistrările din tabelul Lines
        reset_sql = "DELETE FROM sqlite_sequence WHERE name='Lines'"  # Resetează contorul auto-increment pentru tabelul Lines
        # Execută comanda de ștergere
        if self.repository.CommandSQL(delete_sql):
            # Dacă ștergerea a reușit, încearcă să resetezi secvența auto-increment
            if self.repository.CommandSQL(reset_sql):
                return True  # Toate liniile au fost șterse și secvența a fost resetată cu succes
            else:
                return False  # A apărut o eroare la resetarea secvenței
        else:
            return False  # A apărut o eroare la ștergerea liniilor

    def UpdateLine(self, id, new_number, new_stations_list):
        # Check if the line exists
        print("repo")
        print(id, new_number, new_stations_list)
        line_to_find = self.SearchLineByID(id)
        if line_to_find is None:
            print("Line not found, cannot update.")
            return False

        # Update line number
        command_sql = f'UPDATE Lines SET number = "{new_number}" WHERE line_id = {id}'
        self.repository.CommandSQL(command_sql)

        # Remove old stations associations
        command_sql = f'DELETE FROM LineStation WHERE line_id = {id}'
        self.repository.CommandSQL(command_sql)

        # Split the new stations list correctly
        new_stations = [station.strip() for station in new_stations_list.split(",")]

        # Update stations - add new associations and delete old stations if they are not associated with other lines
        for station_name in new_stations:
            # Check if the station already exists
            existing_station = self.repository.GetTable(
                f'SELECT station_id FROM Stations WHERE name = "{station_name}"')
            if not existing_station:
                # Add station if it doesn't exist
                self.add_station(Stations(station_name))
                station_id = self.repository.GetLastRowId()
            else:
                station_id = existing_station[0][0]

            # Add new association in LineStation
            command_sql_association = f'INSERT INTO LineStation (line_id, station_id) VALUES ({id}, {station_id})'
            self.repository.CommandSQL(command_sql_association)

        # Delete stations that are not associated with other lines
        self.delete_unused_stations()

        print("Line updated successfully.")
        return True

    def delete_unused_stations(self):
        # Delete stations that are not associated with other lines
        command_sql = """
            DELETE FROM Stations 
            WHERE station_id NOT IN (SELECT station_id FROM LineStation)
            AND station_id NOT IN (SELECT from_station_id FROM Connections)
            AND station_id NOT IN (SELECT to_station_id FROM Connections)
        """
        self.repository.CommandSQL(command_sql)

    def delete_station(self, station_name):
        # Delete all connections involving this station
        delete_connections_sql = f"""
            DELETE FROM Connections
            WHERE from_station_id = '{station_name}' OR to_station_id = '{station_name}'
        """
        self.repository.CommandSQL(delete_connections_sql)

        # Check and delete station from LineStation
        self.repository.CommandSQL(
            f"DELETE FROM LineStation WHERE station_id IN (SELECT station_id FROM Stations WHERE name = '{station_name}')")

        # Finally, delete the station itself
        delete_station_sql = f"DELETE FROM Stations WHERE name = '{station_name}'"
        if self.repository.CommandSQL(delete_station_sql):
            print(f"Station {station_name} and all related connections have been successfully deleted.")
            return True
        else:
            print(f"Failed to delete station {station_name}.")
            return False

    def delete_connection_by_id(self, connection_id):
        delete_connection_sql = f"DELETE FROM Connections WHERE connection_id = {connection_id}"
        if self.repository.CommandSQL(delete_connection_sql):
            print(f"Connection with ID {connection_id} has been successfully deleted.")
            return True
        else:
            print(f"Failed to delete connection with ID {connection_id}.")
            return False

    def DeleteAllConnections(self):
        try:
            # Execute the SQL command to delete all connections
            delete_sql = "DELETE FROM Connections"
            self.repository.CommandSQL(delete_sql)
            print("All connections have been successfully deleted from the database.")
            return True
        except Exception as e:
            print(f"Error deleting all connections: {e}")
            return False

    def import_connections_from_json(self, file_path):
        try:
            with open(file_path, mode='r') as file:
                connections = json.load(file)
                for connection in connections:
                    from_station = connection['from_station']
                    to_station = connection['to_station']
                    distance = connection['distance']
                    self.addConnection((from_station, to_station, distance))
            print("All connections have been successfully imported from the JSON file.")
        except FileNotFoundError as e:
            print(f"File not found: {e}")
        except Exception as e:
            print(f"Error reading JSON file: {e}")



if __name__ == '__main__':
    # Create a connection to the SQLite database
    db_file = "C:\\Users\\robert\\Desktop\\tema3\\DataBase.db"
    repository = Repository()
    repository.OpeningConnection(db_file)

    network_repo = NetworkRepository()
    network_repo.repository = repository

    # Import connections from JSON
    json_file_path = "C:\\Users\\robert\\Desktop\\tema3\\connections.json"  # Replace with the actual path to your JSON file
    #network_repo.DeleteAllConnections()
    network_repo.import_connections_from_json(json_file_path)

