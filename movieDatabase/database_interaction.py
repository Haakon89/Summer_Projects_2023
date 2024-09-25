import sqlite3

class DatabaseInteraction:
    def __init__(self, database_file='movies.db'):
        self.database_file = database_file

    def view_database(self):
        with sqlite3.connect(self.database_file) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM movies')
            rows = cursor.fetchall()
        return rows

    def add_movie_to_database(self, movie_data):
        with sqlite3.connect(self.database_file) as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO movies (title, release_date, norwegian_title, poster_url) VALUES (?, ?, ?, ?)",
                           (movie_data['title'], movie_data['release_date'], movie_data['norwegian_title'], movie_data['poster_url']))
            conn.commit()

    def remove_movie_from_database(self, movie_title):
        with sqlite3.connect(self.database_file) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM movies WHERE title=?", (movie_title,))
            conn.commit()
