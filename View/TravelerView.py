import tkinter as tk
from tkinter import Scrollbar, messagebox
from tkinter import ttk
from Model.Language import Language
#from PlotApp import PlotApp
from Model.Observer import Observer

class TravelerView(Observer):
    def __init__(self, root):
        self.root = root
        self.root.title("Traveler Page")
        self.root.geometry('1200x500+300+200')
        self.root.configure(bg="#fff")
        self.root.resizable(False, False)

        # Etichetă pentru afișarea liniilor
        self.lines_label = tk.Label(root, text="Welcome To Public Transport App", font=('Microsoft YaHei UI Light', 18, 'bold'))
        self.lines_label.place(x=10, y=10)

        # Buton pentru Find Best Route

        self.best_route_button = tk.Button(root, width=15, pady=2, text="Find Best Route", bg='#57a1f8', border=2, font=('Microsoft YaHei UI Light', 8, 'bold'))
        self.best_route_button.place(x=20, y=140)

        self.start_station_var=tk.StringVar(self.root)
        self.destination_var=tk.StringVar(self.root)

        self.start_station_entry = tk.Entry(root, width=15, borderwidth=5,state="disabled",textvariable=self.start_station_var)
        self.destination_entry = tk.Entry(root, width=15, borderwidth=5,state="disabled",textvariable=self.destination_var)
        self.start_label = tk.Label(root, text='Start', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 11, 'bold'), state="disabled")
        self.end_label = tk.Label(root, text='Destination', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 11, 'bold'), state="disabled")
        self.submit_find_button = tk.Button(root, width=10, pady=2, text="Find Route", bg='#57a1f8', border=2, font=('Microsoft YaHei UI Light', 8, 'bold'))


        # Buton pentru afișarea tuturor liniilor
        self.show_all_button = tk.Button(root, width=15, pady=2, text="Show Lines", bg='#57a1f8', border=2,font=('Microsoft YaHei UI Light', 8, 'bold'))
        self.show_all_button.place(x=20, y=100)


        # Panou pentru afișarea liniilor
        self.lines_panel = tk.Text(root, width=120, height=20, wrap="word", state="disabled")
        self.scrollbar = Scrollbar(root, command=self.lines_panel.yview)
        self.scrollbar_width = 0  # Lungimea initiala a barei de derulare

        self.number_var= tk.StringVar()

        # Câmp de introducere text pentru numărul liniei
        self.line_number_entry = tk.Entry(root, width=10, borderwidth=5,textvariable=self.number_var)
        self.line_number_entry.place(x=240, y=450)
        self.founded_line = tk.Text(root, width=50,borderwidth=5, height=1, wrap="word", state="disabled")

        # Buton pentru căutarea liniei
        self.search_button = tk.Button(root, width=22, pady=2, text="Insert Number to Search", bg='#57a1f8', border=2,font=('Microsoft YaHei UI Light', 8, 'bold'))
        self.search_button.place(x=20, y=445)

        self.line = tk.Text(root,width=90,height=1,wrap="word",state="disabled")

        # Buton pentru deschiderea paginii de login
        self.LoginButton = tk.Button(root, width=15, pady=2, text="Login", bg='#57a1f8', border=2,font=('Microsoft YaHei UI Light', 8, 'bold'))
        self.LoginButton.place(x=1000, y=450)

        self.stations_display = tk.Text(root, width=30, height=5, wrap="word")
        self.stations_display.place(x=370, y=500)
        self.stations_display.config(state="disabled")  # Initially disabled

        self.language_combo_box = ttk.Combobox(root,
                                 values=["English", "Francais", "Italiano"],state="readonly")
        self.language_combo_box.current(0)
        self.language_combo_box.pack(pady=20)
        self.language_combo_box.place(x=900,y=30)
    def update(self,update_type, data=None):
        """
        Implements the Observer update method.
        """
        if update_type == 'show_all_lines':
            pass
        elif update_type == 'search_line':
            pass
        elif update_type=='login_started':
            pass
        elif update_type=='compute_graph':
            self.clear_entries()
        elif update_type=='change_language':
            self.update_language(data)
        else:
            print("Unknown update type received.")

        print(f"Update received: {update_type}, Data: {data}")

    def clear_entries(self):
        """
        Clears the entries for start and destination stations.
        """
        self.start_station_entry.delete(0, 'end')
        self.destination_entry.delete(0, 'end')
        self.start_station_entry.config(state='normal')
        self.destination_entry.config(state='normal')

    def update_language(self,index_of_language):
        self.lines_label.config(text=Language.labels["title"][index_of_language])
        self.best_route_button.config(text=Language.labels["find_best_route"][index_of_language])
        self.submit_find_button.config(text=Language.labels["find_route"][index_of_language])
        self.show_all_button.config(text=Language.labels["show_lines"][index_of_language])
        self.LoginButton.config(text=Language.labels["login"][index_of_language])
        self.search_button.config(text=Language.labels["Insert"][index_of_language])
        self.root.title(Language.labels["traveler_title"][index_of_language])



# if __name__ == "__main__":
#     root = tk.Tk()
#     traveler_vm = TravelerVM()
#     interface = TravelerView(root, traveler_vm)
#     root.mainloop()