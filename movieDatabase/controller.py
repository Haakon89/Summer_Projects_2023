from PIL import ImageTk
import API_interaction
import database_interaction

class Controller:
    def __init__(self, api_interaction, db_interaction):
        self.api_interaction = api_interaction
        self.db_interaction = db_interaction
    
    def add_gui(self, gui):
        self.gui = gui

    def on_add_button_clicked(self):
        movie_title = self.gui.fetch_movie_title()
        movie_data = self.api_interaction.fetch_movie_data_from_api(movie_title)
        if movie_data:
            self.db_interaction.add_movie_to_database(movie_data)
            # Update GUI to show movie has been added
            # You can add more logic here to update the GUI

    def on_remove_button_clicked(self):
        movie_title = self.gui.fetch_movie_title()
        self.db_interaction.remove_movie_from_database(movie_title)
        # Update GUI to show movie has been removed
        # You can add more logic here to update the GUI

    def on_fetch_button_clicked(self):
        movie_title = self.gui.fetch_movie_title()
        movie_data = self.api_interaction.fetch_movie_data_from_api(movie_title)
        
        if movie_data:
            formatted_data = self.format_movie_data(movie_data)
            self.gui.set_movie_info(formatted_data)
            self.update_poster_label(movie_data)
        else:
            self.gui.set_movie_info("Movie not found or an error occurred.")

    def format_movie_data(self, movie_data):
        # Format the movie data into a string and return it
        formatted_data = f"Title: {movie_data.get('title', 'N/A')}\n"
        formatted_data += f"Release Date: {movie_data.get('release_date', 'N/A')}\n"
        formatted_data += f"Norwegian Title: {movie_data.get('norwegian_title', 'N/A')}\n"
        # Add more fields as needed
        return formatted_data

    def update_poster_label(self, movie_data):
        if movie_data and 'poster_url' in movie_data and movie_data['poster_url'] != 'N/A':
            poster_image = self.api_interaction.download_image(movie_data['poster_url'])
            if poster_image:
                poster_photo = ImageTk.PhotoImage(poster_image)
                self.gui.set_poster(poster_photo)
            else:
                self.gui.set_poster(None)  # Clear the label if no image is found
        else:
            self.gui.set_poster(None)  # Clear the label if no image is found
