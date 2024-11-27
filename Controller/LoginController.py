import tkinter as tk
from tkinter import messagebox

from Controller.AdminController import AdminController
from Controller.EmployeeController import EmployeeController
from Model.Repository.NetworkRepository import NetworkRepository
from Model.Repository.UserRepository import UserRepository
from Model.Subject import Subject
from View.LoginView import LoginView
from View.TravelerView import TravelerView
from Model.Language import Language
from Model.Users import Users, UserType

class LoginController(Subject):

    def __init__(self,login_view:LoginView,user_repo:UserRepository):
        super().__init__()
        self.login_view=login_view
        self.user_repo=user_repo
        self.add_observer(login_view)
        self.language=Language()
        self.language.add_observer(login_view)

        self.login_view.go_to_traveler_button.configure(command=self.traveler_page)
        self.login_view.sign_in_button.configure(command=self.sign_in)
        self.login_view.language_combo_box.bind('<<ComboboxSelected>>', self.set_language)


    def set_language(self, event=None):
        index_of_language = self.login_view.language_combo_box.current()
        self.notify_observers('change_language', index_of_language)

    def traveler_page(self):
        print("Traveler page button clicked")
        from Controller.TravelerController import TravelerController

        self.login_view.root.withdraw()  # Ascunde fereastra de login

        # Crează o nouă fereastră pentru TravelerView
        traveler_window = tk.Toplevel()
        traveler_view = TravelerView(traveler_window)

        # Crează un nou TravelerController asociat cu noul TravelerView
        network_repo = NetworkRepository()  # Asigură-te că ai un repository corespunzător
        traveler_controller = TravelerController(traveler_view, network_repo)

        # Setează traveler_window pentru a se închide când se închide fereastra root
        traveler_window.protocol("WM_DELETE_WINDOW", lambda: traveler_window.destroy())

        self.notify_observers("to_traveler_page")

    def sign_in(self):
        username = self.login_view.username_var.get()
        password = self.login_view.password_var.get()
        user_type = self.login_view.user_combo.get()

        print(username,password,user_type)
        user = self.user_repo.SearchUserByUsernameAndPassword(username, password)

        if user:
            if user.get_user_type() == user_type.lower():
                if user_type == "Admin":
                    messagebox.showinfo("Login Successful!", "Welcome Admin!")
                    from View.AdminView import AdminView
                    self.login_view.root.withdraw()
                    admin_window = tk.Toplevel()  # Crează fereastra nouă
                    admin_view = AdminView(admin_window)
                    user_repo = UserRepository()
                    admin_controller=AdminController(admin_view,user_repo)
                elif user_type == "Employee":
                    messagebox.showinfo("Login Successful!", "Welcome Employee!")
                    from View.EmployeeView import EmployeeView
                    self.login_view.root.withdraw()
                    employee_window = tk.Toplevel()
                    empl_view = EmployeeView(employee_window)
                    user_repo = UserRepository()
                    empl_controller=EmployeeController(empl_view,user_repo)

        else:
            messagebox.showinfo("Erorr!", "Wrong User Type!")

        self.notify_observers("sign_in_event")



