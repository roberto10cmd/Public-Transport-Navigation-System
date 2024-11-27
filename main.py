import tkinter as tk
from Model.Repository.NetworkRepository import NetworkRepository
from Model.Subject import Subject
from View.TravelerView import TravelerView
from Controller.TravelerController import TravelerController


def main():
    root = tk.Tk()  # Create the main window

    # Create an instance of your view
    app_view = TravelerView(root)

    # Create an instance of the repository
    network_repo = NetworkRepository()

    # Create the controller and pass it the view and the repository
    app_controller = TravelerController(app_view, network_repo)

    root.mainloop()  # Start the main event loop


if __name__ == "__main__":
    main()
