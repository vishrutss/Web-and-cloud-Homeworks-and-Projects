"""
Favourites  function
"""
from flask import render_template, request, redirect, url_for
from flask.views import MethodView
import gbmodel

class Favourites(MethodView):
    def get(self):
        """
        Displays the entries from the db file
        """
        model = gbmodel.get_model()
        entries = [dict(movie_id=row[0], title=row[1], overview=row[2], language=row[3] ) for row in model.select()]
        return render_template('favourites.html', movies=entries)

    def post(self):
        """
        Deletes a movie from favourites
        """
        movie_id = request.form.get('movie_id')
        model = gbmodel.get_model()
        model.delete(movie_id)
        return redirect(url_for('favourites'))

