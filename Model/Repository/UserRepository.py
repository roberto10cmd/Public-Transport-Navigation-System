
from Model.Repository.Repository import Repository
from Model.Users import Users, UserType


class UserRepository:

    def __init__(self):
        self.repository=Repository()

    def AddUser(self,user):

        if not user.name or not user.username or not user.password or not user.user_type:
            print('Incomplete User fields')
            return False

        command_sql = f'''INSERT INTO Users (name, username, password, user_type)
                                  VALUES ("{user.name}",
                                   "{user.username}",
                                    "{user.password}",
                                     "{user.user_type.value}")'''

        return self.repository.CommandSQL(command_sql)

    def DeleteUser(self, id):

        user_to_delete = self.SearchUserByID(id)
        if user_to_delete is None:
            return False  # Returnăm False pentru că utilizatorul nu există
        else:
            command_sql = f"DELETE FROM Users WHERE id = {id}"
            # Assuming CommandSQL executes the SQL command and returns True if successful
            if self.repository.CommandSQL(command_sql):
                return True  # Deletion successful
            else:
                return False

    def UpdateUser(self,id,user):

        user_to_delete = self.SearchUserByID(id)
        if user_to_delete is None:
            return False  # Returnăm False pentru că utilizatorul nu există
        else:
            command_sql = f'''UPDATE Users SET 
                             name = "{user.name}",
                             username = "{user.username}",
                             password = "{user.password}",
                             user_type = "{user.user_type.value}"
                             WHERE id = {id}'''
            if self.repository.CommandSQL(command_sql):
                return True  # Deletion successful
            else:
                return False

    def SearchUserByID(self, id):
        select_sql = f"SELECT * FROM Users WHERE id = {id}"
        user_data = self.repository.GetTable(select_sql)

        if user_data is None or len(user_data) == 0:
            return None

        user_data = user_data[0]  # Se așteaptă un singur rând
        user = Users(name=user_data[1],
                    username=user_data[2],
                    password=user_data[3],
                    user_type=user_data[4],
                    id=user_data[0])  # ID-ul utilizatorului

        return user

    def UsersList(self):

        select_sql="SELECT * FROM Users ORDER BY id"
        users_table=self.repository.GetTable(select_sql)

        if users_table is None or len(users_table)==0:
            return None

        users_list=[]
        for user_data in users_table:
            user = Users(name=user_data[1],
                        username=user_data[2],
                        password=user_data[3],
                        user_type=user_data[4],
                        id=user_data[0])
            users_list.append(user)   # adaugam user ul curent din tabel in lista care va fi returnata

        return users_list

    def SearchUserByUsernameAndPassword(self, username, password):
        select_sql = f"SELECT * FROM Users WHERE username = '{username}' AND password = '{password}'"
        user_data = self.repository.GetTable(select_sql)

        if user_data is None or len(user_data) == 0:
            return None

        user_data = user_data[0]  # Se așteaptă un singur rând
        user = Users(name=user_data[1],
                    username=user_data[2],
                    password=user_data[3],
                    user_type=user_data[4],
                    id=user_data[0])  # ID-ul utilizatorului
        print(user_data[1])
        return user

    def DeleteAllUsers(self):
        delete_sql = "DELETE FROM Users"  # Șterge toate înregistrările din tabelul Lines
        reset_sql = "DELETE FROM sqlite_sequence WHERE name='Users'"  # Resetează contorul auto-increment pentru tabelul Lines
        # Execută comanda de ștergere
        if self.repository.CommandSQL(delete_sql):
            # Dacă ștergerea a reușit, încearcă să resetezi secvența auto-increment
            if self.repository.CommandSQL(reset_sql):
                return True  # Toate liniile au fost șterse și secvența a fost resetată cu succes
            else:
                return False  # A apărut o eroare la resetarea secvenței
        else:
            return False  # A apărut o eroare la ștergerea liniilor



if __name__ == "__main__":
    # Inițializați conexiunea la baza de date
    db_file = "C:\\Users\\robert\\Desktop\\tema1\\DataBase.db"
    repository = Repository()
    repository.OpeningConnection(db_file)

    # Inițializați UserRepository
    user_repository = UserRepository()

    user_to_add = Users(name="George Stoian", username="geo", password="1234", user_type=UserType.EMPLOYEE)
    success = user_repository.AddUser(user_to_add)
    # if success:
    #     print("Utilizatorul a fost adăugat cu succes.")
    # else:
    #     print("Eroare la adăugarea utilizatorului.")

    # # Ștergeți toți utilizatorii
    # print("\nȘtergem toți utilizatorii...")
    # if user_repository.DeleteAllUsers():
    #     print("Toți utilizatorii au fost șterși cu succes.")
    # else:
    #     print("A apărut o eroare la ștergerea utilizatorilor.")


    # Închideți conexiunea la baza de date
    repository.ClosingConnection()
