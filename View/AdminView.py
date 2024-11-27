import os
from tkinter import *
from tkinter import messagebox, ttk
import tkinter as tk
from Model.Language import Language
from Model.Observer import Observer
from View.LoginView import LoginView
from Model.Repository import UserRepository as UserRepo


class AdminView(Observer):
    def __init__(self, root):
        self.root = root
        self.root.title("Admin Page")
        self.root.geometry('1200x500+300+200')
        self.root.configure(bg="#fff")
        self.root.resizable(False, False)
        self.update_interval = 500
        self.update_started = False  # Variabilă pentru a verifica dacă actualizarea a început



        frame = Frame(root, width=280, height=350, bg="white")
        frame.place(x=480, y=70)

        heading = Label(root, text='Operations', fg='#57a1f8', bg='white',
                        font=('Microsoft YaHei UI Light', 23, 'bold'))
        heading.place(x=20, y=5)

        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(BASE_DIR, 'admin_logo.png')
        self.img = PhotoImage(file=image_path)
        # Afisare imagine
        self.image_label = Label(root, image=self.img, bg='white')
        self.image_label.place(x=730, y=10)


        self.users_display = tk.Text(root, width=60, height=15, wrap="word", state="disabled")
        self.scrollbar = Scrollbar(root, command=self.users_display.yview)
        self.scrollbar_width = 0  # Lungimea initiala a barei de derulare

        # Buton pentru ștergerea unui utilizator

        self.show_users = Button(root, width=15, pady=7, text="Show Users", bg='#57a1f8', border=2,
                                 font=('Microsoft YaHei UI Light', 11, 'bold'))
        self.show_users.place(x=20, y=240)


        ###############################################################################
        ## butoanele mari de add/delete/update

        # Buton pentru adăugarea unui utilizator
        self.add_button = Button(root, width=15, pady=7, text="Add Employee", bg='#57a1f8', border=2,
                            font=('Microsoft YaHei UI Light', 11, 'bold'))
        self.add_button.place(x=20, y=60)


        # Buton pentru ștergerea unui utilizator
        self.delete_button = Button(root, width=15, pady=7, text="Delete Employee", bg='#57a1f8', border=2,
                               font=('Microsoft YaHei UI Light', 11, 'bold'))
        self.delete_button.place(x=20, y=120)

        # Buton pentru actualizarea unui utilizator
        self.update_button = Button(root, width=15, pady=7, text="Update Employee", bg='#57a1f8', border=2,
                               font=('Microsoft YaHei UI Light', 11, 'bold'))
        self.update_button.place(x=20, y=180)


        ###############################################################################
        # Gadgeturi pt butonul de Add Employeer

        self.name_var = StringVar()
        self.username_var = StringVar()
        self.password_var = StringVar()

        # Label uri pt adaugarea unui user

        self.name_label = Label(root, text='Name', fg='#57a1f8', bg='white',
                                font=('Microsoft YaHei UI Light', 11, 'bold'), state="disabled")
        self.username_label = Label(root, text='Username', fg='#57a1f8', bg='white',
                                    font=('Microsoft YaHei UI Light', 11, 'bold'), state="disabled")
        self.pass_label = Label(root, text='Password', fg='#57a1f8', bg='white',
                                font=('Microsoft YaHei UI Light', 11, 'bold'), state="disabled")

        # TextField uri pentru adaugarea unui user

        self.name_txt_field = tk.Entry(root, width=25, borderwidth=2, state="disabled", textvariable=self.name_var)

        self.username_txt_field = tk.Entry(root, width=25, borderwidth=2, state="disabled",
                                           textvariable=self.username_var)

        self.pass_txt_field = tk.Entry(root, width=25, borderwidth=2, state="disabled", textvariable=self.password_var)

        self.submit_add_button = Button(root, width=15, pady=2, text="Submit Add Op", bg='#57a1f8', border=2,
                                        font=('Microsoft YaHei UI Light', 8, 'bold'))

        ###############################################################################


        # Gadgeturi pentru delete Employee

        self.id_var = StringVar()

        # Label uri pt stergerea unui user

        self.Id_label = Label(root, text='Id', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 11, 'bold'),
                              state="disabled")

        # TextField uri pentru stergerea unui user

        self.Id_txt_field = tk.Entry(root, width=25, borderwidth=2, state="disabled", textvariable=self.id_var)

        self.submit_delete_button = Button(root, width=15, pady=2, text="Submit Delete Op", bg='#57a1f8', border=2,
                                           font=('Microsoft YaHei UI Light', 8, 'bold'))


        ###############################################################################

        # Gadgeturi pentru update Employee

        self.id_update_var= StringVar()
        self.name_update_var = StringVar()
        self.username_update_var = StringVar()
        self.password_update_var = StringVar()

        # Label uri pt actualizarea unui user

        self.id_label_Update = Label(root, text='Id', fg='#57a1f8', bg='white',
                                     font=('Microsoft YaHei UI Light', 11, 'bold'), state="disabled")
        self.name_label_Update = Label(root, text='Name', fg='#57a1f8', bg='white',
                                       font=('Microsoft YaHei UI Light', 11, 'bold'), state="disabled")
        self.username_label_Update = Label(root, text='Username', fg='#57a1f8', bg='white',
                                           font=('Microsoft YaHei UI Light', 11, 'bold'), state="disabled")
        self.pass_label_Update = Label(root, text='Password', fg='#57a1f8', bg='white',
                                       font=('Microsoft YaHei UI Light', 11, 'bold'), state="disabled")

        # TextField uri pentru actualizarea unui user

        self.id_txt_field_Update = tk.Entry(root, width=25, borderwidth=2, state="disabled",textvariable=self.id_update_var)

        self.name_txt_field_Update = tk.Entry(root, width=25, borderwidth=2, state="disabled",textvariable=self.name_update_var)

        self.username_txt_field_Update = tk.Entry(root, width=25, borderwidth=2, state="disabled",textvariable=self.username_update_var)

        self.pass_txt_field_Update = tk.Entry(root, width=25, borderwidth=2, state="disabled",textvariable=self.password_update_var)

        self.submit_update_button = Button(root, width=15, pady=2, text="Submit Update Op", bg='#57a1f8', border=2,
                                           font=('Microsoft YaHei UI Light', 8, 'bold'))

        ###############################################################################

        self.LoginButton = Button(root, width=15, pady=7, text="Login Page", bg='#57a1f8', border=2,
                             font=('Microsoft YaHei UI Light', 11, 'bold'))
        self.LoginButton.place(x=1040, y=430)

        self.language_combo_box = ttk.Combobox(root,
                                               values=["English", "Francais", "Italiano"], state="readonly")
        self.language_combo_box.current(0)
        self.language_combo_box.pack(pady=20)
        self.language_combo_box.place(x=750, y=30)

        self.users_filter_combo_box = ttk.Combobox(root,
                                               values=["Admin", "Employee"], state="readonly")
        self.users_filter_combo_box.current(0)
        self.users_filter_combo_box.pack(pady=20)
        self.users_filter_combo_box.place(x=600, y=30)

    def update(self,update_type,data=None):

        """
        Implements the Observer update method.
        """
        if update_type=="to_traveler_page":
            print("s a facut update")
        elif update_type=="sign_in_event":
            print("S a realizat Sign in")
        elif update_type=="change_language":
            self.update_language(data)
        elif update_type=="users_change":
            for user in data:
                user_details = f"User {user.id}: {user.name}, {user.username}, {user.password}, {user.user_type}\n"
                self.users_display.insert(tk.END, user_details)
        else:
            print("Unknown update type received.")

        print(f"Update received: {update_type}, Data: {data}")

    def update_language(self,index_of_language):
        self.root.title(Language.labels["admin_title"][index_of_language])  # Actualizare titlu fereastră
        self.show_users.configure(text=Language.labels["Show Users"][index_of_language])
        self.add_button.configure(text=Language.labels["Add Employee"][index_of_language])
        self.delete_button.configure(text=Language.labels["Delete Employee"][index_of_language])
        self.update_button.configure(text=Language.labels["Update Employee"][index_of_language])
        self.name_label.configure(text=Language.labels["Name"][index_of_language])
        self.username_label.configure(text=Language.labels["Username"][index_of_language])
        self.pass_label.configure(text=Language.labels["Password"][index_of_language])
        self.submit_add_button.configure(text=Language.labels["submit_add_button"][index_of_language])
        self.Id_label.configure(text=Language.labels["id_coon_label"][index_of_language])
        self.name_label_Update.configure(text=Language.labels["Name"][index_of_language])
        self.username_label_Update.configure(text=Language.labels["Username"][index_of_language])
        self.pass_label_Update.configure(text=Language.labels["Password"][index_of_language])
        self.submit_update_button.configure(text=Language.labels["submit_update_button_update"][index_of_language])
        self.submit_delete_button.configure(text=Language.labels["submit_delete_button"][index_of_language])
        self.LoginButton.configure(text=Language.labels["login_title"][index_of_language])
        self.id_label_Update.configure(text=Language.labels["id_coon_label"][index_of_language])
