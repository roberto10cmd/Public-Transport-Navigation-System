# Public Transportation Routing System

This is a Python-based application designed to help users plan optimal routes using public transportation. The system uses the MVC (Model-View-Controller) architecture and is implemented using several key libraries, including SQLite for database management, Tkinter for the graphical user interface (GUI), and NetworkX for graph-based routing algorithms.

## Features

- **Multi-role support**: The application supports three types of users: Traveler, Employee, and Administrator.
- **Route Management**: Employees can manage transport lines, including adding, updating, and deleting lines and stations.
- **Shortest Path Calculation**: Travelers can calculate the shortest route between two stations.
- **Graphical Representation**: Displays connectivity between stations and routes using NetworkX and Matplotlib.
- **Data Export**: Employees can export transport line data in various formats such as CSV, JSON, XML, and DOC.
- **Language Support**: The application supports multiple languages, and users can switch languages through a dropdown menu.
- **Login System**: The application includes a secure login system with authentication based on user roles.

## Architecture

The application follows the **Model-View-Controller (MVC)** design pattern:

- **Model**: Contains the business logic and data manipulation, including interaction with the SQLite database.
- **View**: The graphical user interface, built using Tkinter, which displays data and captures user interactions.
- **Controller**: Manages user actions, communicates with the model, and updates the view accordingly.

### Database

The database consists of the following tables:

- **User**: Stores user data (name, username, password, role).
- **Lines**: Stores information about public transport lines.
- **LineStation**: Stores information about stations on each transport line.
- **Connections**: Represents the connections between stations.

### Use Cases

- **Traveler**: View available routes, calculate the shortest path, view transport line details.
- **Employee**: Manage transport lines, add/update/delete stations, export data, and view station connectivity graphs.
- **Administrator**: Manage users (add/remove/update users), change settings, and view overall system status.

## Tools and Libraries

- **Python**: The programming language used to develop the application.
- **SQLite**: A lightweight database used to store user data, transport lines, stations, and connections.
- **Tkinter**: The library used for creating the graphi
