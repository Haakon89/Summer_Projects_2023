import tkinter as tk
from GUI import MovieDatabaseGUI
from controller import Controller
from API_interaction import APIHandler
from database_interaction import DatabaseInteraction
import movie_database as md

def main():
    # Initialize the main application window
    root = tk.Tk()
    root.title("Movie Database")

    # Initialize the database
    md.create_database()  # Assuming this function sets up your database

    # Initialize API Handler and Database Interaction
    api_handler = APIHandler()
    db_interaction = DatabaseInteraction()

    # Initialize Controller with references to the GUI, API handler, and DB interaction
    controller = Controller(api_handler, db_interaction)

    # Initialize GUI
    app_gui = MovieDatabaseGUI(root, controller, db_interaction)

    controller.add_gui(app_gui)
    # Start the application
    root.mainloop()

if __name__ == "__main__":
    main()
