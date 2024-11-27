
import sqlite3

class Repository:
    def __init__(self):
        self.connection=None
        self.db_file="C:\\Users\\robert\\Desktop\\tema3\\DataBase.db"

    def getConnection(self):
        return self.connection

    def setConnection(self,conn):
        self.connection=conn

    def OpeningConnection(self,db_file):
        if self.connection is None:
            self.connection = sqlite3.connect(db_file)

        elif not self.connection:
            self.connection = sqlite3.connect(db_file)

    def ClosingConnection(self):
        if self.connection:
            self.connection.close()
            self.connection=None

    def CommandSQL(self,commandSQL):
        result=True
        try:
            self.OpeningConnection(self.db_file)
            cursor = self.connection.cursor()
            cursor.execute(commandSQL)
            self.connection.commit()
            self.last_row_id = cursor.lastrowid  # Actualizează atribute cu ultimul ID inserat

        except sqlite3.Error as e:
            print("Error executing SQL command: ",e)
            result = False
        finally:
            self.ClosingConnection()
        return result

    def GetTable(self, commandSQL):
        result = None
        try:
            self.OpeningConnection(self.db_file)
            cursor = self.connection.cursor()
            cursor.execute(commandSQL)
            result = cursor.fetchall()

        except sqlite3.Error as e:
            print("Error fetching data: ", e)
        finally:
            self.ClosingConnection()
        return result

    def GetLastRowId(self):
        return self.last_row_id  # Returnează ultimul ID inserat




if __name__ == "__main__":
    # Inițializăm obiectul de tip Repository
    repository = Repository()

    # Deschidem conexiunea către baza de date
    repository.OpeningConnection(repository.db_file)



    # Închidem conexiunea către baza de date
    repository.ClosingConnection()
