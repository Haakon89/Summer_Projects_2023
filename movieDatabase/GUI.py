# GUI.py
import tkinter as tk
from tkinter import ttk

class MovieDatabaseGUI:
    def __init__(self, root, controller, db_interaction):
        self.root = root
        self.controller = controller
        self.db_interaction = db_interaction
        self.setup_gui()

    def setup_gui(self):
        self.root.title("Movie Database")

        # Outer frame
        outer_frame = ttk.Frame(self.root, padding="10")
        outer_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Inner frame for centered input field
        input_frame = ttk.Frame(outer_frame)
        input_frame.grid(row=0, column=0, columnspan=2)

        movie_title_label = ttk.Label(input_frame, text="Enter Movie Title:")
        movie_title_label.grid(row=0, column=0)
        self.movie_title_entry = ttk.Entry(input_frame, width=30)
        self.movie_title_entry.grid(row=0, column=1)
        fetch_button = ttk.Button(input_frame, text="Fetch Movie Data", command=self.controller.on_fetch_button_clicked)
        fetch_button.grid(row=0, column=2)

        add_button = ttk.Button(outer_frame, text="Add to Database", command=self.controller.on_add_button_clicked)
        add_button.grid(row=2, column=0)

        remove_button = ttk.Button(outer_frame, text="Remove from Database", command=self.controller.on_remove_button_clicked)
        remove_button.grid(row=2, column=1)

        # GUI setup for Treeview
        columns = ("Title", "Release Date", "Norwegian Title", "Poster URL")
        self.tree = ttk.Treeview(outer_frame, columns=columns, show='headings')
        self.tree.grid(row=3, column=0, columnspan=2)

        # Movie Info Text and Poster Label
        self.movie_info_text = tk.Text(outer_frame, height=15, width=50)
        self.movie_info_text.grid(row=1, column=0)
        self.movie_info_text.tag_configure('bold', font=('Arial', 10, 'bold'))  # Define a bold tag
        self.movie_info_text.config(state=tk.DISABLED)

        self.poster_label = ttk.Label(outer_frame)
        self.poster_label.grid(row=1, column=1, sticky=tk.N)

        # Define headings
        for col in columns:
            self.tree.heading(col, text=col)

        # Button to refresh data from database
        refresh_button = ttk.Button(outer_frame, text="Refresh Data", command=self.update_treeview)
        refresh_button.grid(row=2, column=2)

    def fetch_movie_title(self):
        return self.movie_title_entry.get()

    def set_movie_info(self, text):
        self.movie_info_text.config(state=tk.NORMAL)
        self.movie_info_text.delete(1.0, tk.END)
        self.movie_info_text.insert(tk.END, text, 'bold')
        self.movie_info_text.config(state=tk.DISABLED)

    def set_poster(self, image):
        self.poster_label.config(image=image)
        self.poster_label.image = image

    def update_treeview(self):
        data = self.db_interaction.view_database()
        # Clear the treeview
        for item in self.tree.get_children():
            self.tree.delete(item)
        # Insert new data
        for row in data:
            self.tree.insert("", tk.END, values=row)

# The mainloop will be started in main.py, so it's removed from here.
