
from tkinter import *
from tkinter import messagebox
from tkinter import Label,PhotoImage
from tkinter import ttk

from Model.Language import Language
from Model.Observer import Observer
import tkinter as tk
import os


class EmployeeView(Observer):

    def __init__(self, root):
        self.root = root
        self.root.title("Employee Page")
        self.root.geometry('1200x500+300+200')
        self.root.configure(bg="#fff")
        self.root.resizable(False, False)
        # Etichetă pentru titlu

        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(BASE_DIR, 'employee_3.png')

        self.img = PhotoImage(file=image_path)

        # Afisare imagine
        self.image_label = Label(root, image=self.img, bg='white')
        self.image_label.place(x=800, y=10)


        frame = Frame(root, width=280, height=350, bg="white")
        frame.place(x=480, y=70)

        self.heading = Label(root, text='Operations', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
        self.heading.place(x=20, y=5)

        self.save_csv = Button(root, width=15, pady=7, text="Save As CSV", bg='#57a1f8', border=2,
                                 font=('Microsoft YaHei UI Light', 11, 'bold'))

        self.save_csv.place(x=20, y=240)

        self.save_json = Button(root, width=15, pady=7, text="Save As JSON", bg='#57a1f8', border=2,
                               font=('Microsoft YaHei UI Light', 11, 'bold'))
        self.save_json.place(x=20, y=300)

        self.save_xml = Button(root, width=15, pady=7, text="Save As XML", bg='#57a1f8', border=2,
                                font=('Microsoft YaHei UI Light', 11, 'bold'))
        self.save_xml.place(x=20, y=360)

        self.save_doc = Button(root, width=15, pady=7, text="Save As DOC", bg='#57a1f8', border=2,
                               font=('Microsoft YaHei UI Light', 11, 'bold'))
        self.save_doc.place(x=20, y=420)

        self.LoginButton = Button(root, width=15, pady=7, text="Login Page", bg='#57a1f8', border=2,
                             font=('Microsoft YaHei UI Light', 11, 'bold'))
        self.LoginButton.place(x=1040, y=430)



        # Buton pentru adăugarea unei linii
        self.add_button = Button(root,width=15, pady=7, text="Add Line ",bg='#57a1f8',border=2, font=('Microsoft YaHei UI Light', 11, 'bold'))
        self.add_button.place(x=20,y=60)

        # Buton pentru ștergerea unei linii
        self.delete_button = Button(root, width=15, pady=7, text="Delete Line", bg='#57a1f8', border=2,font=('Microsoft YaHei UI Light', 11, 'bold'))
        self.delete_button.place(x=20, y=120)

        # Buton pentru actualizarea unei linii
        self.update_button = Button(root, width=15, pady=7, text="Update Line", bg='#57a1f8', border=2,font=('Microsoft YaHei UI Light', 11, 'bold'))
        self.update_button.place(x=20, y=180)


        ## Gadgeturi pentru adaugarea unei conexiuni
        self.add_conn_button = Button(root, width=15, pady=7, text="Add Connection ", bg='#57a1f8', border=2,
                                      font=('Microsoft YaHei UI Light', 11, 'bold'))
        self.add_conn_button.place(x=220, y=300)

        self.start_station_var=StringVar()
        self.end_station_var=StringVar()
        self.distance_var=StringVar()

        self.start_station_field = tk.Entry(root, width=25, borderwidth=2,state="disabled",textvariable=self.start_station_var)
        self.end_station_field = tk.Entry(root, width=25, borderwidth=2,state="disabled",textvariable=self.end_station_var)
        self.distance_field = tk.Entry(root, width=25, borderwidth=2,state="disabled",textvariable=self.distance_var)

        self.start_station_label = Label(root, text='Start Station', fg='#57a1f8', bg='white',font=('Microsoft YaHei UI Light', 11, 'bold'),state="disabled")
        self.end_station_label = Label(root, text='End Station', fg='#57a1f8', bg='white',font=('Microsoft YaHei UI Light', 11, 'bold'),state="disabled")
        self.distance_label = Label(root, text='Distance', fg='#57a1f8', bg='white',font=('Microsoft YaHei UI Light', 11, 'bold'),state="disabled")

        self.submit_conn_button = Button(root, width=15, pady=2, text="Submit Add Conn", bg='#57a1f8', border=2,font=('Microsoft YaHei UI Light', 8, 'bold'))

        ################################################################

        ## Gadgeturi pentru delete la conexiune

        self.id_conn_var=StringVar()

        self.id_coon_label=Label(root, text='Connection Id', fg='#57a1f8', bg='white',font=('Microsoft YaHei UI Light', 11, 'bold'),state="disabled")

        self.id_coon_field=tk.Entry(root, width=25, borderwidth=2,state="disabled",textvariable=self.id_conn_var)

        self.delete_conn_button = Button(root, width=15, pady=7, text="Delete Connection ", bg='#57a1f8', border=2,
                                      font=('Microsoft YaHei UI Light', 11, 'bold'))
        self.delete_conn_button.place(x=220, y=360)

        self.show_graph_button = Button(root, width=15, pady=7, text="Show Chart", bg='#57a1f8', border=2,
                                         font=('Microsoft YaHei UI Light', 11, 'bold'))
        self.show_graph_button.place(x=220, y=420)

        self.submit__delete_conn_button = Button(root, width=18, pady=2, text="Submit Delete Conn", bg='#57a1f8', border=2,font=('Microsoft YaHei UI Light', 8, 'bold'))


        ##################################################################




        # Gadgeturi pt butonul de Add Line

        self.number_var= StringVar()
        self.stations_list_var= StringVar()

        self.number_label = Label(root, text='Number', fg='#57a1f8', bg='white',font=('Microsoft YaHei UI Light', 11, 'bold'),state="disabled")
        self.stations_label = Label(root, text='Stations', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 11, 'bold'),state="disabled")

        self.number_txt_field = tk.Entry(root, width=25, borderwidth=2,state="disabled",textvariable=self.number_var)

        self.station_txt_field = tk.Entry(root, width=25, borderwidth=2,state="disabled",textvariable=self.stations_list_var)

        self.submit_add_button = Button(root, width=15, pady=2, text="Submit Add Op", bg='#57a1f8', border=2,font=('Microsoft YaHei UI Light', 8, 'bold'))

        ########

        # Gadgeturi pt butonul de Delete Line
        self.id_delete_var=StringVar()
        self.Id_label = Label(root, text='Id', fg='#57a1f8', bg='white',font=('Microsoft YaHei UI Light', 11, 'bold'),state="disabled")
        self.Id_txt_field = tk.Entry(root, width=25, borderwidth=2, state="disabled",textvariable=self.id_delete_var)

        self.submit_delete_button = Button(root, width=15, pady=2, text="Submit Delete Op", bg='#57a1f8', border=2,font=('Microsoft YaHei UI Light', 8, 'bold'))


        # Gadgeturi pt butonul de Update Line

        self.number_label_update = Label(root, text='Number', fg='#57a1f8', bg='white',
                                  font=('Microsoft YaHei UI Light', 11, 'bold'), state="disabled")
        self.stations_label_update = Label(root, text='Stations', fg='#57a1f8', bg='white',
                                    font=('Microsoft YaHei UI Light', 11, 'bold'), state="disabled")

        self.id_update_var=StringVar(root)
        self.number_update_var=StringVar(root)
        self.stations_update_var=StringVar(root)

        self.number_txt_field_update = tk.Entry(root, width=25, borderwidth=2, state="disabled",textvariable=self.number_update_var)

        self.station_txt_field_update = tk.Entry(root, width=25, borderwidth=2, state="disabled",textvariable=self.stations_update_var)

        self.submit_update_button_update = Button(root, width=15, pady=2, text="Submit Update Op", bg='#57a1f8', border=2,font=('Microsoft YaHei UI Light', 8, 'bold'))

        self.id_label_update_update=Label(root, text='Id', fg='#57a1f8', bg='white',
                                  font=('Microsoft YaHei UI Light', 11, 'bold'), state="disabled")

        self.id_txt_update_update=tk.Entry(root, width=25, borderwidth=2, state="disabled",textvariable=self.id_update_var)

        # ComboBox pentru selectia limbii curente
        self.language_combo_box = ttk.Combobox(root,
                                               values=["English", "Francais", "Italiano"], state="readonly")
        self.language_combo_box.current(0)
        self.language_combo_box.pack(pady=20)
        self.language_combo_box.place(x=700, y=30)
    def update(self,update_type, data=None):
        """
        Implements the Observer update method.
        """
        if update_type =='line_added':
            self.number_txt_field.delete(0, 'end')
            self.number_txt_field.config(state='normal')
            self.station_txt_field.delete(0, 'end')
            self.station_txt_field.config(state='normal')
        elif update_type =='line_deleted':
            self.Id_txt_field.delete(0, 'end')
            self.Id_txt_field.config(state='normal')
        elif update_type=='line_updated':
            self.id_txt_update_update.delete(0, 'end')
            self.id_txt_update_update.config(state='normal')
            self.number_txt_field_update.delete(0, 'end')
            self.number_txt_field_update.config(state='normal')
            self.station_txt_field_update.delete(0, 'end')
            self.station_txt_field_update.config(state='normal')
        elif update_type=='connection_deleted':
            self.id_coon_field.delete(0, 'end')
            self.id_coon_field.config(state='normal')
        elif update_type=='connection_added':
            self.start_station_field.delete(0, 'end')
            self.start_station_field.config(state='normal')
            self.end_station_field.delete(0, 'end')
            self.end_station_field.config(state='normal')
            self.distance_field.delete(0, 'end')
            self.distance_field.config(state='normal')
        elif update_type=='saved_as_csv':
            pass
        elif update_type=='saved_as_json':
            pass
        elif update_type=='saved_as_xml':
            pass
        elif update_type=='saved_as_doc':
            pass
        elif update_type=='to_login_page':
            pass
        elif update_type=='change_language':
            self.update_language(data)
        else:
            print("Unknown update type received.")

        print(f"Update received: {update_type}, Data: {data}")



    def update_language(self, index_of_language):
        self.root.title(Language.labels["employee_title"][index_of_language])
        self.heading.config(text=Language.labels["headingE"][index_of_language])
        self.save_csv.config(text=Language.labels["save_csv"][index_of_language])
        self.save_json.config(text=Language.labels["save_json"][index_of_language])
        self.save_xml.config(text=Language.labels["save_xml"][index_of_language])
        self.save_doc.config(text=Language.labels["save_doc"][index_of_language])
        self.LoginButton.config(text=Language.labels["LoginButtonEmployee"][index_of_language])
        self.add_button.config(text=Language.labels["add_button_empl"][index_of_language])
        self.delete_button.config(text=Language.labels["delete_button_empl"][index_of_language])
        self.update_button.config(text=Language.labels["update_button_empl"][index_of_language])
        self.start_station_label.config(text=Language.labels["start_station_label"][index_of_language])
        self.end_station_label.config(text=Language.labels["end_station_label"][index_of_language])
        self.distance_label.config(text=Language.labels["distance_label"][index_of_language])
        self.add_conn_button.config(text=Language.labels["add_conn_button"][index_of_language])
        self.submit_conn_button.config(text=Language.labels["submit_conn_button"][index_of_language])
        self.id_coon_label.config(text=Language.labels["id_coon_label"][index_of_language])
        self.delete_conn_button.config(text=Language.labels["delete_conn_button"][index_of_language])
        self.submit__delete_conn_button.config(text=Language.labels["submit__delete_conn_button"][index_of_language])
        self.number_label.config(text=Language.labels["number_label"][index_of_language])
        self.stations_label.config(text=Language.labels["stations_label"][index_of_language])
        self.submit_add_button.config(text=Language.labels["submit_add_button"][index_of_language])
        self.Id_label.config(text=Language.labels["id_coon_label"][index_of_language])
        self.submit_delete_button.config(text=Language.labels["submit_delete_button"][index_of_language])
        self.number_label_update.config(text=Language.labels["number_label_update"][index_of_language])
        self.stations_label_update.config(text=Language.labels["stations_label_update"][index_of_language])
        self.submit_update_button_update.config(text=Language.labels["submit_update_button_update"][index_of_language])

