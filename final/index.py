"""
This opens index.html
"""
from flask import render_template
from flask.views import MethodView
import gbmodel
import os
import requests

class Index(MethodView):
    def get(self):
        """
        Redirects to index.html
        """
        model = gbmodel.get_model()
        tmdb_api_key = os.environ['TMDB_API_KEY']
        url = f'https://api.themoviedb.org/3/discover/movie?api_key={tmdb_api_key}&sort_by=popularity.desc'
        response = requests.get(url)
        print("HEHE")
        if response.status_code == 200:
            data = response.json()
            movies = data['results']
            print("HEHE")
        else:
            movies = []

        return render_template('index.html', movies=movies)
