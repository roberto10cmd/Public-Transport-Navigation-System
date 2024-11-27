from Model.Lines import Lines
from Model.Repository.Repository import Repository

class LineRepository:

    def __init__(self):
        self.repository=Repository()

    def AddLine(self,lines):
        stations_list = lines.get_station_list()
        if stations_list is None:
            stations_list = []

        command_sql = f'''INSERT INTO Lines (number, stations)
         VALUES ({lines.get_number()},
          "{','.join(stations_list)}")'''

        return self.repository.CommandSQL(command_sql)

    def DeleteLine(self,id):
        line_to_find = self.SearchLineByID(id)
        if line_to_find is None:
            return False  # Returnăm False pentru că linia nu există
        else:
            commnand_sql=f" Delete FROM Lines WHERE id ={id} "
            if self.repository.CommandSQL(commnand_sql):
                return True  # Deletion successful
            else:
                return False

    def UpdateLine(self,id,line):

            line_to_find = self.SearchLineByID(id)
            if line_to_find is None:
                return False  # Returnăm False pentru că linia nu există
            else:
                command_sql = f'''UPDATE Lines SET 
                                 number = "{line.number}",
                                 stations = "{line.stations_list}"
                                 WHERE id = {id}'''
                if self.repository.CommandSQL(command_sql):
                    return True  # Deletion successful
                else:
                    return False

    def LinesList(self):

        select_sql="SELECT * FROM Lines ORDER BY id"
        lines_table=self.repository.GetTable(select_sql)

        if lines_table is None or len(lines_table)==0:
            return None

        lines_list = []

        for line_data in lines_table:
            line_number = line_data[1]
            stations = line_data[2].split(',') if line_data[2] else []
            line = Lines(number=line_number, stations_list=stations,id=line_data[0])
            lines_list.append(line)

        return lines_list

    def SearchLineByID(self, id):
        select_sql = f"SELECT * FROM Lines WHERE id = {id}"
        line_data = self.repository.GetTable(select_sql)

        if line_data is None or len(line_data) == 0:
            return None

        line_data = line_data[0]  # Se așteaptă un singur rând
        line = Lines(number=line_data[1],
                     stations_list=line_data[2].split(','),  # Convertim șirul de stații înapoi într-o listă
                     id=line_data[0])  # ID-ul liniei

        return line



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

# if __name__ == "__main__":
#
#     db_file = "C:\\Users\\robert\\Desktop\\tema1\\DataBase.db"
#     repository = Repository()
#     repository.OpeningConnection(db_file)
#     line_repository = LineRepository()
#
#     # Apelarea metodei de ștergere a tuturor liniilor
#     result = line_repository.DeleteAllLines()
#     if result:
#         print("Toate liniile au fost șterse cu succes.")
#     else:
#         print("A apărut o eroare la ștergerea liniilor.")
#
#
#     repository.ClosingConnection()


