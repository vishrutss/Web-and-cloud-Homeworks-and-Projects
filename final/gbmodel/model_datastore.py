# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from .Model import Model
from datetime import datetime
from google.cloud import datastore

def from_datastore(entity):
    """Translates Datastore results into the format expected by the
    application.

    Datastore typically returns:
        [Entity{key: (kind, id), prop: val, ...}]

    This returns:
        [ movie_id, title, overview, language ]
    where name, email, and message are Python strings
    and where date is a Python datetime
    """
    if not entity:
        return None
    if isinstance(entity, list):
        entity = entity.pop()
    return [entity['movie_id'],entity['title'],entity['overview'],entity['language']]

class model(Model):
    def __init__(self):
        """
        Initializes the model object.
        It creates a connection to the Datastore client.
        Args: None
        Returns: None
        """
        self.client = datastore.Client('cloud-sharma-vishrut')

    def select(self):
        """
        Retrieves all entities of kind 'Movies' from the Datastore.
        Args: None
        Returns: entities (list): A list of dictionaries representing the entities.
        """
        query = self.client.query(kind = 'Movies')
        entities = list(map(from_datastore,query.fetch()))
        return entities

    def insert(self,movie_id,title,overview,language):
        """
        Inserts a new entity with the given details into the Datastore.
        Args:
            movie_id (str): The ID of the movie.
            title (str): The title of the movie.
            overview (str): The overview of the movie.
            language (str): The language of the movie.
        Returns: bool: True if the entity is successfully inserted, False otherwise.
        """
        key = self.client.key('Movies')
        rev = datastore.Entity(key)
        rev.update( {
            'movie_id': movie_id,
            'title' : title,
            'overview' : overview,
            'language' : language,
            })
        self.client.put(rev)
        return True

    def delete(self, movie_id):
        """
        Deletes an entity with the given movie_id from the Datastore.
        Args: movie_id (str): The ID of the movie to be deleted.
        Returns: bool: True if the entity is successfully deleted, False otherwise.
        """
        query = self.client.query(kind='Movies')
        for entity in query.fetch():
            if entity['movie_id'] == movie_id:
                self.client.delete(entity.key)

