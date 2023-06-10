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
        Adds selected entry into the database
        Redirect to index when completed.
        """
        data = request.get_json()
        movie_id = data.get('movie_id')
        title = data.get('title')
        overview = data.get('overview')
        language = data.get('language')
        
        model = gbmodel.get_model()
        entries = [dict(movie_id=row[0], title=row[1], overview=row[2], language=row[3]) for row in model.select()]
        
        if not any(entry['movie_id'] == movie_id for entry in entries):
            model.insert(movie_id, title, overview, language)
        return redirect(url_for('index'))
