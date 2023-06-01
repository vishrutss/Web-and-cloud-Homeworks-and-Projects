"""
This is used to add to favourites
"""
from flask import redirect, request, url_for, render_template
from flask.views import MethodView
import gbmodel

class Submit(MethodView):
    def post(self):
        """
        Accepts POST requests, and processes the request;
        Redirect to index when completed.
        """
        data = request.get_json()
        movie_id = data.get('movie_id')
        title = data.get('title')
        overview = data.get('overview')
        language = data.get('language')
        
        model = gbmodel.get_model()
        model.insert(movie_id, title, overview, language)
        return redirect(url_for('index'))
