import csv
import tkinter as tk
from tkinter import messagebox

from Model.PlotApp import PlotApp
from Model.Repository.NetworkRepository import NetworkRepository
from Model.Repository.UserRepository import UserRepository
from Model.Subject import Subject
from View.LoginView import LoginView
from View.TravelerView import TravelerView
from Model.Language import Language

class TravelerController(Subject):
    def __init__(self, traveler_view: TravelerView, network_repo: NetworkRepository):
        super().__init__()
        self.traveler_view = traveler_view
        self.network_repo = network_repo
        self.add_observer(traveler_view)
        self.language=Language()
        self.language.add_observer(traveler_view)
        # Set up bindings between view buttons and controller methods
        self.traveler_view.best_route_button.configure(command=self.show_gadgets)
        self.traveler_view.show_all_button.configure(command=self.show_all_lines)
        self.traveler_view.search_button.configure(command=self.search_line)
        self.traveler_view.submit_find_button.configure(command=self.compute_graph)
        self.traveler_view.LoginButton.configure(command=self.open_login_page)
        self.traveler_view.language_combo_box.bind('<<ComboboxSelected>>', self.set_language)

    def set_language(self,event=None):
        print("schimbarea limbii")
        index_of_language=self.traveler_view.language_combo_box.current()
        self.notify_observers('change_language',index_of_language)

    def show_all_lines(self):
        lines_list = self.network_repo.LinesList()  # Assuming this method fetches and returns a list of dictionaries
        sorted_list=[]
        if lines_list is not None:
            sorted_list = sorted(lines_list, key=lambda x: int(x['number']))

        self.traveler_view.lines_panel.place(x=160, y=100)
        self.scrollbar_width = 20
        self.traveler_view.scrollbar.place(x=1120, y=100, height=320, width=self.scrollbar_width)
        self.traveler_view.lines_panel.config(state="normal")
        self.traveler_view.lines_panel.delete('1.0', tk.END)
        print(lines_list)

        if sorted_list:
            for line in sorted_list:
                self.traveler_view.lines_panel.insert(tk.END, f"Line {line['number']}: {line['stations']}\n")
        else:
            self.traveler_view.lines_panel.insert(tk.END, "No lines available.\n")

        self.traveler_view.lines_panel.config(state="disabled")
        self.notify_observers('show_all_lines', {'lines': lines_list})

    def search_line(self):
        line_number = self.traveler_view.number_var.get()
        print("Searching for line number:", line_number)
        stations =self.network_repo.station_by_number(line_number)
        print("Stations found:", stations)
        formatted_stations = ', '.join(stations)
        self.traveler_view.founded_line.place(x=350,y=450)
        self.traveler_view.founded_line.config(state="normal")
        self.traveler_view.founded_line.delete('1.0', tk.END)
        if stations:
            self.traveler_view.founded_line.insert(tk.END,formatted_stations)
        else:
            if line_number:
                message="Line with "+str(line_number)+" not found."
            else:
                message="Insert Number of Line!"

            self.traveler_view.founded_line.insert(tk.END,message)
            self.notify_observers('search_line', {'line_number': line_number, 'result': stations})

    def find_shortest_path(self, path_data):
        start_station, end_station = path_data
        connections = self.network_repo.get_all_connections()

        # Create a graph in the form of a dictionary
        graph = {}
        for from_station, to_station, distance in connections:
            if from_station not in graph:
                graph[from_station] = {}
            if to_station not in graph:
                graph[to_station] = {}  # Ensure to_station is also a key in the graph
            graph[from_station][to_station] = float(distance)

        print(graph)

        # Check if start or end stations are in the graph
        if start_station not in graph or end_station not in graph:
            return f"Error: One or both stations '{start_station}' or '{end_station}' not found in network."

        # Implementing Dijkstra's Algorithm with an edge count consideration
        shortest_paths = {
            start_station: (None, 0, 0)}  # Dictionary stores tuples (previous_node, total_distance, edge_count)
        current_station = start_station
        visited_stations = set()

        while current_station != end_station:
            visited_stations.add(current_station)
            destinations = graph[current_station]  # Assuming current_station is always in the graph now
            current_distance, current_edge_count = shortest_paths[current_station][1], shortest_paths[current_station][
                2]

            for next_station in destinations:
                distance_via_current = current_distance + destinations[next_station]
                new_edge_count = current_edge_count + 1
                if next_station not in shortest_paths:
                    shortest_paths[next_station] = (current_station, distance_via_current, new_edge_count)
                else:
                    known_distance, known_edge_count = shortest_paths[next_station][1], shortest_paths[next_station][2]
                    if (distance_via_current < known_distance) or (
                            distance_via_current == known_distance and new_edge_count < known_edge_count):
                        shortest_paths[next_station] = (current_station, distance_via_current, new_edge_count)

            next_destinations = {station: shortest_paths[station] for station in shortest_paths if
                                 station not in visited_stations}
            if not next_destinations:
                return "Route Not Possible"
            current_station = min(next_destinations, key=lambda k: (
            next_destinations[k][1], next_destinations[k][2]))  # Compare by distance and then edge count

        # Work back through destinations in shortest path
        path = []
        while current_station is not None:
            path.append(current_station)
            next_station = shortest_paths[current_station][0]
            current_station = next_station
        # Reverse path
        path = path[::-1]
        print("DDD")
        print(path)
        return path


    def compute_graph(self):
        self.traveler_view.start_station_entry.config(state="normal")
        self.traveler_view.destination_entry.config(state="normal")
        start = self.traveler_view.start_station_var.get()
        end = self.traveler_view.destination_var.get()
        print(f"Start Station: '{start}' | Destination Station: '{end}'")  # Debug output

        path = self.find_shortest_path((start, end))
        print("Computed Path:", path)

        if isinstance(path, list) and path:
            self.open_graph_view(path)
        elif isinstance(path, str) and 'Error' in path:
            messagebox.showerror("Error", path)  # Display an error message box if the path is an error message
        else:
            messagebox.showinfo("No Path Found", f"No route found from {start} to {end}")
            self.open_graph_view([])  # Optionally open the graph with no highlighted path

        self.notify_observers('compute_graph', {'start': start, 'end': end})

    def open_graph_view(self, path):
        graph_window = tk.Toplevel(self.traveler_view.root)
        graph_window.title("Visualized Path")
        try:
            plot_app = PlotApp(graph_window, self.network_repo, highlight_path=path)
        except Exception as e:
            print("Error initializing PlotApp:", e)
            messagebox.showerror("Plot Error", f"Failed to plot graph: {str(e)}")

    def show_gadgets(self):
        self.traveler_view.start_label.place(x=50, y=210)
        self.traveler_view.start_label.config(state="normal")
        self.traveler_view.end_label.place(x=25, y=270)
        self.traveler_view.end_label.config(state="normal")
        self.traveler_view.start_station_entry.place(x=25, y=240)
        self.traveler_view.start_station_entry.config(state="normal")
        self.traveler_view.destination_entry.place(x=25, y=300)
        self.traveler_view.destination_entry.config(state="normal")
        self.traveler_view.submit_find_button.place(x=34, y=340)
        self.traveler_view.submit_find_button.config(state="normal")

    def open_login_page(self):
        print("Opening login page...")
        from Controller.LoginController import LoginController

        # Ascunde temporar fereastra principală (TravelerView)
        self.traveler_view.root.withdraw()

        # Crează o nouă fereastră Toplevel pentru LoginView
        login_window = tk.Toplevel()
        login_view = LoginView(login_window)
        user_repo = UserRepository()  # Asigură-te că ai un repository corespunzător
        login_controller = LoginController(login_view, user_repo)

        # Asigură-te că atunci când login_window este închis, fereastra principală este reafișată

        self.notify_observers('login_started', {})

    def load_connections_from_file(self, file_path):
        """
        Load connections from a CSV file and insert them into the database.
        The CSV file should have the format: from_station,to_station,distance
        """
        try:
            with open(file_path, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if len(row) == 3:
                        from_station, to_station, distance = row
                        from_station_name, to_station_name, distance = connection_data

                        self.network_repo.addConnection(from_station, to_station, float(distance))
            messagebox.showinfo("Success", "Connections loaded successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load connections: {str(e)}")
