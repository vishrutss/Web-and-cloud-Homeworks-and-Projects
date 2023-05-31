"""
Display function
"""
from flask import render_template
from flask.views import MethodView
import gbmodel
import requests
import openai
import os
from googleapiclient.discovery import build


class Display(MethodView):
    def fetch_movie_title(self, movie_id):
        tmdb_api_key = os.environ['TMDB_API_KEY']
        url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={tmdb_api_key}'
        response = requests.get(url)
        if response.status_code == 200:
            movie_data = response.json()
            movie_title = {
                'title': movie_data['title'],
            }
            return movie_title
        else:
            return None
    
    def get_trailer(self, movie_title):
        youtube_api_key = os.environ['YOUTUBE_API_KEY']
        youtube = build('youtube', 'v3', developerKey=youtube_api_key)
        search_response = youtube.search().list(
            q=f"{movie_title} trailer",
            part='id',
            maxResults=1,
            type='video'
        ).execute()

        trailer_id = search_response['items'][0]['id']['videoId']
        return trailer_id

    def get(self, movie_id):
        # Fetch movie details for the provided movie ID
        movie_title = self.fetch_movie_title(movie_id)
        trailer_id = self.get_trailer(movie_title)
        return render_template('display.html', movie=movie_title, trailer_id=trailer_id)
    


