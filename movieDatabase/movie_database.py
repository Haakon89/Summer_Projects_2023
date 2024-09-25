import sqlite3

def create_database():
    conn = sqlite3.connect('movies.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS movies
                 (title TEXT, release_date TEXT, norwegian_title TEXT, poster_url TEXT)''')
    conn.commit()
    conn.close()