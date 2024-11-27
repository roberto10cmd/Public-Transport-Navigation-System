from tkinter import *
from tkinter import messagebox
from tkinter import Label, PhotoImage
from tkinter import ttk
from Model.Language import Language
from Model.Observer import Observer
import tkinter as tk
import os


class LoginView(Observer):
    def __init__(self, root):
        self.root = root
        self.root.title("Login Page")
        self.root.geometry('925x500')
        self.root.configure(bg="#fff")
        self.root.resizable(False, False)

        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(BASE_DIR, 'login.png')

        self.img = PhotoImage(file=image_path)

        # Afisare imagine
        self.image_label = Label(root, image=self.img, bg='white')
        self.image_label.image = self.img  # Keep a reference!
        self.image_label.place(x=50, y=50)
        print("Image path:", image_path)
        print("Is the file accessible:", os.path.exists(image_path))
        # Frame
        frame = Frame(root, width=350, height=350, bg="white")
        frame.place(x=480, y=70)

        # Titlu
        self.heading = Label(frame, text='Sign in', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
        self.heading.place(x=100, y=5)

        # Câmp de introducere text

        def on_enter(e):
            self.user.delete(0, 'end')

        def on_leave(e):
            name = self.user.get()
            if name == ' ':
                self.user.insert(0, 'Username')

        self.username_var = StringVar()
        self.password_var = StringVar()

        self.user = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11),textvariable=self.username_var)
        self.user.place(x=30, y=80)
        self.user.insert(0, 'Username')
        self.user.bind('<FocusIn>', on_enter)
        self.user.bind('<FocusOut>', on_leave)

        Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

        def on_enter(e):
            self.code.delete(0, 'end')

        def on_leave(e):
            name = self.code.get()
            if name == ' ':
                self.code.insert(0, 'Password')

        self.code = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11),textvariable=self.password_var)
        self.code.place(x=30, y=150)
        self.code.insert(0, 'Password')
        self.code.bind('<FocusIn>', on_enter)
        self.code.bind('<FocusOut>', on_leave)

        Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

        self.sign_in_button=Button(frame, width=39, pady=7, text='Sign In', bg='#57a1f8', border=0)
        self.sign_in_button.place(x=35, y=204)

        self.go_to_traveler_button = Button(frame, width=20, pady=7, text='Go to Traveler Page', bg='#57a1f8', border=0)
        self.go_to_traveler_button.place(x=170, y=310)

        self.selectuser = Label(frame, text='Select type of user', fg='#57a1f8', bg='white',
                           font=('Microsoft YaHei UI Light', 11, 'bold'))
        self.selectuser.place(x=0, y=250)

        self.user_combo = ttk.Combobox(frame, values=['Employee', 'Admin'], width=18, state='readonly')
        self.user_combo.current(0)  # Setează valoarea implicită
        self.user_combo.place(x=185, y=273)

        self.language_combo_box = ttk.Combobox(root,
                                               values=["English", "Francais", "Italiano"], state="readonly")
        self.language_combo_box.current(0)
        self.language_combo_box.pack(pady=20)
        self.language_combo_box.place(x=750, y=30)

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
        else:
            print("Unknown update type received.")

        print(f"Update received: {update_type}, Data: {data}")

    def update_language(self,index_of_language):
        self.heading.config(text=Language.labels["signin"][index_of_language])
        self.selectuser.config(text=Language.labels["user_type"][index_of_language])
        self.go_to_traveler_button.config(text=Language.labels["traveler_button"][index_of_language])
        self.sign_in_button.config(text=Language.labels["signin"][index_of_language])
        self.root.title(Language.labels["login_title"][index_of_language])  # Actualizare titlu fereastră
        # Actualizare text Username și Password
        self.user.delete(0, END)
        self.user.insert(0, Language.labels["username_placeholder"][index_of_language])
        self.code.delete(0, END)
        self.code.insert(0, Language.labels["password_placeholder"][index_of_language])