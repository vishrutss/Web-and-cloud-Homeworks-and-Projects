"""
A simple study space entry flask app.
Data is stored in a SQLite database that looks something like the following:

+------------+------------------+------------+----------------+-------+
| Building Name        | Building Code | floor  | room number | rating|
+============+==================+============+----------------+-------+
| Engineering Building | FAB           | 5      | 512         | 4.2   |
+------------+------------------+------------+----------------+-------+

This can be created with the following SQL (see bottom of this file):

    create table study_space (bname text, bcode text, floor integer, room_num integer, rating real);

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
            cursor.execute("select count(bcode) from study_space")
        except sqlite3.OperationalError:
            cursor.execute("create table study_space (bname text, bcode text, floor integer, room_num integer, rating real)")
        cursor.close()

    def select(self):
        """
        Gets all rows from the database
        Each row contains: bname, bcode, floor, room_num, rating
        :return: List of lists containing all rows of database
        """
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM study_space")
        return cursor.fetchall()

    def insert(self, name, email, message):
        """
        Inserts entry into database
        :param bname: String
        :param bcode: String
        :param floor: Integer
        :param room_num: Integer
        :param rating: Float
        :return: True
        :raises: Database errors on connection and insertion
        """
        params = {'bname':bname, 'bcode':bcode, 'floor':floor, 'room_num':room_num, 'rating':rating}
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute("insert into guestbook (bname, bcode, floor, room_num, rating) VALUES (:bname, :bcode, :floor, :room_num, :rating)", params)

        connection.commit()
        cursor.close()
        return True
