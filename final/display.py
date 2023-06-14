"""
Display function
"""
from flask import render_template
from flask.views import MethodView
import gbmodel
import requests
import os
from googleapiclient.discovery import build


class Display(MethodView):
    def fetch_movie_title(self, movie_id):
        """
        Fetches the movie title from the TMDB API
        :param movie_id: String
        :return: movie_title if movie_id is valid, None otherwise
        """
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
        """
        Fetches the id of the trailer from the YouTube API
        :param movie_title: String
        :return: trailer's YouTube video id
        """
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

    def get_likes_and_views(self, trailer_id):
        """
        Fetches the number of likes and views for the YouTube video
        :param trailer_id: String
        :return: Dictionary containing likes and views
        """
        youtube_api_key = os.environ['YOUTUBE_API_KEY']
        youtube = build('youtube', 'v3', developerKey=youtube_api_key)
        video_response = youtube.videos().list(
            part='statistics',
            id=trailer_id
        ).execute()

        statistics = video_response['items'][0]['statistics']
        likes = int(statistics['likeCount'])
        views = int(statistics['viewCount'])

        return {'likes': likes, 'views': views}

    def get(self, movie_id):
        """
        Fetches movie title and trailer id from fetch_movie_title(), and get_trailer() functions respectively
        and redirects to display.html
        :param movie_id: String
        """
        movie_title = self.fetch_movie_title(movie_id)
        trailer_id = self.get_trailer(movie_title)
        likes_and_views = self.get_likes_and_views(trailer_id)
        return render_template('display.html', movie=movie_title, trailer_id=trailer_id, likes_and_views=likes_and_views)
    


