import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import ttk

from Model.Repository.NetworkRepository import NetworkRepository

class PlotApp:
    def __init__(self, root, network_repo, highlight_path=None):
        self.root = root
        self.network_repo = network_repo
        self.root.title("Traseu între stații")
        self.highlight_path = highlight_path if highlight_path else []

        # Prepare the plot
        plt.figure(figsize=(12, 8))
        plt.clf()  # Clear any existing plot

        # Fetch connection data
        connections = self.network_repo.get_all_connections()

        # Create a NetworkX directed graph
        G = nx.DiGraph()

        # Add nodes and edges based on connections
        for from_station, to_station, distance in connections:
            G.add_node(from_station)
            G.add_node(to_station)
            G.add_edge(from_station, to_station, weight=distance)

        # Position nodes using a layout with seed for reproducibility
        pos = nx.shell_layout(G)

        # Draw edges with curved style if there are bi-directional edges
        for (u, v, d) in G.edges(data=True):
            if G.has_edge(v, u):  # Check for reverse edge
                # Draw curved edges with arrows
                nx.draw_networkx_edges(G, pos, edgelist=[(u, v)], connectionstyle='arc3, rad=0.1',
                                       edge_color='gray', arrowstyle='-|>', arrowsize=10, width=2)
            else:
                # Draw straight edges
                nx.draw_networkx_edges(G, pos, edgelist=[(u, v)], edge_color='gray', arrowstyle='-|>', arrowsize=10)

        # Highlight paths if specified
        if self.highlight_path and len(self.highlight_path) > 1:
            highlighted_edges = [(u, v) for (u, v) in zip(self.highlight_path, self.highlight_path[1:])]
            nx.draw_networkx_edges(G, pos, edgelist=highlighted_edges, edge_color='red', arrowstyle='-|>', arrowsize=20, width=2)

        # Draw labels
        nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold')
        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

        # Create the canvas
        fig = plt.gcf()
        self.canvas = FigureCanvasTkAgg(fig, master=self.root)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Close button
        self.close_button = ttk.Button(self.root, text="Close", command=self.root.destroy)
        self.close_button.pack(side=tk.BOTTOM)

if __name__ == "__main__":
    root = tk.Tk()
    network_repo = NetworkRepository()  # Ensure this class is implemented correctly to fetch connection data
    highlight_path = []  # Ensure the stations are in the correct directional order
    app = PlotApp(root, network_repo, highlight_path=highlight_path)
    root.mainloop()