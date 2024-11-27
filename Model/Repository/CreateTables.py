import sqlite3

class CreateTables:
    def __init__(self, db_file):
        self.db_file = db_file

    def create_tables(self):
        try:
            conn = sqlite3.connect(self.db_file)
            cursor = conn.cursor()

            cursor.execute('''CREATE TABLE IF NOT EXISTS Users (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    name TEXT,
                                    username TEXT,
                                    password TEXT,
                                    user_type TEXT
                                )''')

            # Creare tabela Stations
            cursor.execute('''CREATE TABLE IF NOT EXISTS Stations (
                                            station_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                            name TEXT NOT NULL
                                        )''')

            # Creare tabela Connections
            cursor.execute('''CREATE TABLE IF NOT EXISTS Connections (
                                            connection_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                            from_station_id INTEGER NOT NULL,
                                            to_station_id INTEGER NOT NULL,
                                            distance REAL NOT NULL,
                                            FOREIGN KEY (from_station_id) REFERENCES Stations(station_id),
                                            FOREIGN KEY (to_station_id) REFERENCES Stations(station_id)
                                        )''')

            # Creare tabela Lines
            cursor.execute('''CREATE TABLE IF NOT EXISTS Lines (
                                            line_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                            number TEXT NOT NULL UNIQUE
                                        )''')

            # Creare tabela LineStation
            cursor.execute('''CREATE TABLE IF NOT EXISTS LineStation (
                                            line_id INTEGER,
                                            station_id INTEGER,
                                            PRIMARY KEY (line_id, station_id),
                                            FOREIGN KEY (line_id) REFERENCES Lines(line_id),
                                            FOREIGN KEY (station_id) REFERENCES Stations(station_id)
                                        )''')

            # Creare tabela TransportNetwork

            conn.commit()
            print("Tabelele au fost create cu succes!")
        except sqlite3.Error as e:
            print(f"Eroare la crearea tabelelor: {str(e)}")
        finally:
            if conn:
                conn.close()

# Exemplu de utilizare:
if __name__ == "__main__":
    db_file = "C:\\Users\\robert\\Desktop\\tema3\\DataBase.db"
    tables_creator = CreateTables(db_file)
    tables_creator.create_tables()
