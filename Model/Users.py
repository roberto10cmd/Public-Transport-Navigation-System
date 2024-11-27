from enum import Enum

class UserType(Enum):
    EMPLOYEE="employee"
    ADMIN="admin"

class Users:
    def __init__(self,name,username,password,user_type,id=None):
        self.name=name
        self.id=id
        self.username=username
        self.password=password

        #if user_type=="employee" or user_type=="admin" or user_type=="EMPLOYEE" or user_type=="ADMIN" :
        self.user_type=user_type
        #else:
            #raise ValueError("Invalid user Type")

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_id(self):
        return self.id

    def get_username(self):
        return self.username

    def set_username(self, username):
        self.username = username

    def get_password(self):
        return self.password

    def set_password(self, password):

        self.password = password

    def get_user_type(self):
        return self.user_type

    def __str__(self):
        return f"Name: {self.name}, ID: {self.id}, Username: {self.username}, User Type: {self.user_type}"




