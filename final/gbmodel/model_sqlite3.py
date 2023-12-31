"""
A simple movie trailer viewer flask app.
Data is stored in a SQLite database that looks something like the following:

+------------+------------------+------------+----------------+
| Movie ID   | Movie Title      | Overview         | Language |
+============+==================+============+----------------+
| 1          | John Wick        | *Movie synopsis* | en       |
+------------+------------------+------------+----------------+

This can be created with the following SQL (see bottom of this file):

    create table movies (movie_id text, title text, overview text, language text);

"""
from .Model import Model
import sqlite3
DB_FILE = 'entries.db'    # file for our Database

class model(Model):
    def __init__(self):
        # Make sure our database exists
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        try:
            cursor.execute("select count(movie_id) from movies")
        except sqlite3.OperationalError:
            cursor.execute("create table movies (movie_id text, title text, overview text, language text)")
        cursor.close()

    def select(self):
        """
        Gets all rows from the database
        Each row contains: movie_id, title, overview, language
        :return: List of lists containing all rows of database
        """
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM movies")
        return cursor.fetchall()

    def insert(self, movie_id, title, overview, language):
        """
        Inserts entry into database
        :param movie_id: String
        :param title: String
        :param overview: String
        :param language: String
        :return: True
        :raises: Database errors on connection and insertion
        """
        params = {'movie_id':movie_id, 'title':title, 'overview':overview, 'language':language}
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("insert into movies (movie_id, title, overview, language) VALUES (:movie_id, :title, :overview, :language)", params)

        connection.commit()
        cursor.close()
        return True

    def delete(self, movie_id):
        """
        Deletes an entry from the database
        :param movie_id: String
        :return: True
        :raises: Database errors on connection and deletion
        """
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("DELETE FROM movies WHERE movie_id = ?", (movie_id,))
        connection.commit()
        cursor.close()
        return True

