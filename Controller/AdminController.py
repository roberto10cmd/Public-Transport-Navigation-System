import tkinter as tk
from Model.Repository.UserRepository import UserRepository
from Model.Subject import Subject
from Model.Users import Users, UserType
from View.AdminView import AdminView
from Model.Language import Language

class AdminController(Subject):

    def __init__(self,admin_view:AdminView,user_repo:UserRepository):
        super().__init__()
        self.admin_view=admin_view
        self.user_repo=user_repo
        self.add_observer(admin_view)
        self.language = Language.get_instance()  # Obține instanța Singleton a clasei Language
        self.language.add_observer(admin_view)

        # Set up bindings between view buttons and controller methods

        self.admin_view.LoginButton.configure(command=self.open_login_page)
        self.admin_view.add_button.configure(command=self.show_add_gadgets_method)
        self.admin_view.delete_button.configure(command=self.show_delete_gadgets_method)
        self.admin_view.update_button.configure(command=self.show_update_gadgets_method)
        self.admin_view.submit_add_button.configure(command=self.on_add_employee)
        self.admin_view.submit_delete_button.configure(command=self.on_delete_employee)
        self.admin_view.submit_update_button.configure(command=self.on_update_employee)
        self.admin_view.show_users.configure(command=self.show_users_method)
        self.admin_view.language_combo_box.bind('<<ComboboxSelected>>', self.set_language)
        self.admin_view.users_filter_combo_box.bind('<<ComboboxSelected>>',self.filter_by_type_of_users)



    def open_login_page(self):
        print("s a ajuns in metoda de pe buton")
        from Controller.LoginController import LoginController
        from View.LoginView import LoginView
        self.admin_view.root.withdraw()
        login_window = tk.Toplevel()
        login_view = LoginView(login_window)
        user_repo = UserRepository()
        login_controller = LoginController(login_view, user_repo)
        login_window.protocol("WM_DELETE_WINDOW", lambda: login_window.destroy())
        self.notify_observers("to_login_page")

    def show_add_gadgets_method(self):
        self.make_invizible_delete()
        self.make_invizible_update()
        self.admin_view.name_label.place(x=120, y=355)
        self.admin_view.name_label.config(state="normal")
        self.admin_view.username_label.place(x=88, y=395)
        self.admin_view.username_label.config(state="normal")
        self.admin_view.pass_label.place(x=92, y=435)
        self.admin_view.pass_label.config(state="normal")
        self.admin_view.name_txt_field.place(x=180, y=360)
        self.admin_view.name_txt_field.config(state="normal")
        self.admin_view.username_txt_field.place(x=180, y=400)
        self.admin_view.username_txt_field.config(state="normal")
        self.admin_view.pass_txt_field.place(x=180, y=440)
        self.admin_view.pass_txt_field.config(state="normal")
        self.admin_view.submit_add_button.place(x=350, y=395)
        self.admin_view.submit_add_button.config(state="normal")

    def show_delete_gadgets_method(self):
        self.make_invizible_add()
        self.make_invizible_update()
        self.admin_view.Id_label.place(x=120, y=355)
        self.admin_view.Id_label.config(state="normal")
        self.admin_view.Id_txt_field.place(x=180, y=360)
        self.admin_view.Id_txt_field.config(state="normal")
        self.admin_view.submit_delete_button.place(x=350, y=395)
        self.admin_view.submit_delete_button.config(state="normal")

    def show_update_gadgets_method(self):
        self.make_invizible_delete()
        self.make_invizible_add()
        self.admin_view.id_label_Update.place(x=140, y=315)
        self.admin_view.id_txt_field_Update.place(x=180, y=315)
        self.admin_view.id_txt_field_Update.config(state="normal")
        self.admin_view.name_label_Update.place(x=120, y=355)
        self.admin_view.name_label_Update.config(state="normal")
        self.admin_view.username_label_Update.place(x=88, y=395)
        self.admin_view.username_label_Update.config(state="normal")
        self.admin_view.pass_label_Update.place(x=92, y=435)
        self.admin_view.pass_label_Update.config(state="normal")
        self.admin_view.id_txt_field_Update.place(x=180, y=320)
        self.admin_view.name_txt_field_Update.place(x=180, y=360)
        self.admin_view.name_txt_field_Update.config(state="normal")
        self.admin_view.username_txt_field_Update.place(x=180, y=400)
        self.admin_view.username_txt_field_Update.config(state="normal")
        self.admin_view.pass_txt_field_Update.place(x=180, y=440)
        self.admin_view.pass_txt_field_Update.config(state="normal")
        self.admin_view.submit_update_button.place(x=350, y=395)
        self.admin_view.submit_update_button.config(state="normal")



    def make_invizible_add(self):
        # Facem widget-urile pentru adăugare invizibile
        self.admin_view.name_label.place_forget()
        self.admin_view.username_label.place_forget()
        self.admin_view.pass_label.place_forget()
        self.admin_view.name_txt_field.place_forget()
        self.admin_view.username_txt_field.place_forget()
        self.admin_view.pass_txt_field.place_forget()
        self.admin_view.submit_add_button.place_forget()

    def make_invizible_delete(self):

        self.admin_view.Id_label.place_forget()
        self.admin_view.Id_txt_field.place_forget()
        self.admin_view.submit_delete_button.place_forget()

    def make_invizible_update(self):
        # Facem widget-urile pentru update invizibile
        self.admin_view.id_label_Update.place_forget()
        self.admin_view.id_txt_field_Update.place_forget()
        self.admin_view.name_label_Update.place_forget()
        self.admin_view.username_label_Update.place_forget()
        self.admin_view.pass_label_Update.place_forget()
        self.admin_view.name_txt_field_Update.place_forget()
        self.admin_view.username_txt_field_Update.place_forget()
        self.admin_view.pass_txt_field_Update.place_forget()
        self.admin_view.submit_update_button.place_forget()

    def on_add_employee(self):
        name = self.admin_view.name_var.get()
        username = self.admin_view.username_var.get()
        password = self.admin_view.password_var.get()
        user = Users(name, username, password, UserType.EMPLOYEE)
        self.user_repo.AddUser(user)
    def on_delete_employee(self):
        id = self.admin_view.id_var.get()
        self.user_repo.DeleteUser(id)
    def on_update_employee(self):
        id = self.admin_view.id_update_var.get()
        name= self.admin_view.name_update_var.get()
        username= self.admin_view.username_update_var.get()
        password=self.admin_view.password_update_var.get()
        user = Users(name, username, password, UserType.EMPLOYEE)
        self.user_repo.UpdateUser(id, user)

    def show_users_method(self):

        users_list = self.user_repo.UsersList()

        self.admin_view.users_display.place(x=240, y=60)
        self.scrollbar_width = 20
        self.admin_view.scrollbar.place(x=720, y=60, height=100, width=self.scrollbar_width)
        self.admin_view.users_display.config(state="normal")
        self.admin_view.users_display.delete('1.0', tk.END)
        if users_list:
            for user in users_list:
                user_details = f"User {user.id}: {user.name}, {user.username}, {user.password}, {user.user_type}\n"
                self.admin_view.users_display.insert(tk.END, user_details)
        else:
            self.admin_view.users_display.insert(tk.END, "No Users available.\n")

        self.admin_view.users_display.config(state="disabled")
        self.notify_observers("users_change",users_list)

    def set_language(self, event=None):
        index_of_language = self.admin_view.language_combo_box.current()
        self.notify_observers('change_language', index_of_language)

    def filter_by_type_of_users(self, event=None):
        selected_user_type = self.admin_view.users_filter_combo_box.get()
        users_list = self.user_repo.UsersList()

        self.admin_view.users_display.place(x=240, y=60)
        self.scrollbar_width = 20
        self.admin_view.scrollbar.place(x=720, y=60, height=100, width=self.scrollbar_width)
        self.admin_view.users_display.config(state="normal")
        self.admin_view.users_display.delete('1.0', tk.END)

        if users_list:
            filtered_users = [user for user in users_list if user.user_type == selected_user_type.lower()]
            if filtered_users:
                for user in filtered_users:
                    user_details = f"User {user.id}: {user.name}, {user.username}, {user.password}, {user.user_type}\n"
                    self.admin_view.users_display.insert(tk.END, user_details)
            else:
                self.admin_view.users_display.insert(tk.END, f"No {selected_user_type} users available.\n")
        else:
            self.admin_view.users_display.insert(tk.END, "No Users available.\n")

        self.admin_view.users_display.config(state="disabled")
