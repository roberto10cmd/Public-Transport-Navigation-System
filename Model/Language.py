from Model.Subject import Subject

class Language(Subject):

    labels =  {
        "title": ["Welcome to Traveler Page!", "Bienvenue sur la page des voyageurs!", "Benvenuti nella Pagina dei Viaggiatori!"],
        "find_route": ["Find Route","Trouver L'Itinéraire","Trovare Il Percorso"],
        "show_lines": ["Show Lines", "Afficher les lignes", "Mostra linee"],
        "find_best_route":["Find Best Route", "Trouver le meilleur itinéraire", "Trova il miglior percorso"],
        "login":["Login","Se Connecter","Entrando"],
        "Insert":["Insert Number to Search","Insérer le numéro à rechercher","Inserisci il numero da cercare"],
        "signin":["Sign In","Se Connecter","Registrazione"],
        "user_type":["Select type of user","Sélectionnez le type d'utilisateur","Seleziona il tipo di utente"],
        "traveler_button":["Go to Traveler Page","Aller à la page Voyageur","Vai alla pagina del viaggiatore"],
        "login_title":["Login Page","Page de connexion","Pagina di login"],
        "employee_title":["Employee Page","Page des employés","Pagina dei dipendenti"],
        "traveler_title":["Traveler Page","Page Voyageur","Pagina del viaggiatore"],
        "username_placeholder":["Username","Nom d'utilisateur","Nome utente"],
        "password_placeholder":["Password","Mot de passe","Parola d'ordine"],
        "headingE":["Operations","Opérations","Operazioni"],
        "save_csv":["Save As CSV","Enregistrer au format CSV","Salva come CSV"],
        "save_json":["Save As JSON","Enregistrer au format JSON","Salva come JSON"],
        "save_xml":["Save As XML","Enregistrer au format XML","Salva come XML"],
        "save_doc":["Save As DOC","Enregistrer au format DOC","Salva come DOC"],
        "LoginButtonEmployee":["Login Page","Page de connexion","Pagina di login"],
        "add_button_empl":["Add Line","Ajouter une ligne","Aggiungi linea"],
        "delete_button_empl":["Delete Line","Supprimer la ligne","Elimina riga"],
        "update_button_empl":["Update Line","Mettre à jour la ligne","Linea di aggiornamento"],
        "start_station_label":["Start Station","Station de départ","Inizio stazione"],
        "end_station_label":["End Station","Station finale","Stazione finale"],
        "distance_label":["Distance","Distance","Distanza"],
        "add_conn_button":["Add Connection ","Ajouter une connexion","Aggiungi connessione"],
        "submit_conn_button":["Submit Add Conn","Soumettre Ajouter une connexion","Invia Aggiungi conn"],
        "id_coon_label":["Id","Identifiant","Id"],
        "delete_conn_button":["Delete Connection","Supprimer la connexion","Elimina connessione"],
        "submit__delete_conn_button":["Submit Delete Conn","Soumettre Supprimer la connexion","Invia Elimina conn"],
        "number_label":["Number","Nombre","Numero"],
        "stations_label":["Stations","Gares","Stazioni"],
        "submit_add_button":["Submit Add Op","Soumettre Ajouter une opération","Invia Aggiungi Op"],
        "submit_delete_button":["Submit Delete Op","Soumettre l'opération de suppression","Invia Elimina Op"],
        "number_label_update":["Number","Nombre","Numero"],
        "stations_label_update":["Stations","Gares","Stazioni"],
        "submit_update_button_update":["Submit Update Op","Soumettre une opération de mise à jour","Invia aggiornamento Op"],
        "admin_title":["Admin Page","Page d'administration","Pagina di amministrazione"],
        "Show Users":["Show Users","Afficher les utilisateurs","Mostra utenti"],
        "Add Employee": ["Add Employee","Ajouter un employé","Aggiungi dipendente"],
        "Delete Employee": ["Delete Employee","Supprimer un employé","Elimina dipendente"],
        "Update Employee": ["Update Employee","Mettre à jour l'employé","Aggiorna dipendente"],
        "Name": ["Name","Nom","Nome"],
        "Username": ["Username","Nom d'utilisateur","Nome utente"],
        "Password": ["Password","Mot de passe","Parola d'ordine"],
    }

    _instance=None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, '_initialized'):
            super().__init__()
            self._initialized = True

    @staticmethod
    def get_instance():
        if Language._instance is None:
            Language._instance = Language()
        return Language._instance





