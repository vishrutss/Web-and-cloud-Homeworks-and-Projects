class Model():
    def select(self):
        """
        Gets all entries from the database
        :return: Tuple containing all rows of database
        """
        pass

    def insert(self, movie_id, title, overview, language):
        """
        Inserts entry into database
        :param movie_id: String
        :param title: String
        :param overview: String
	:param language: String
        :return: none
        :raises: Database errors on connection and insertion
        """
        pass

    def delete(self, movie_id):
        """
        Deletes an entry from the database based on the movie_id
        :param movie_id: String
        :return: True if the deletion is successful, False otherwise
        :raises: Database errors on connection and deletion
        """
        pass
