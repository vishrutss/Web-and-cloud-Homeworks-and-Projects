"""
This opens index.html
"""
from flask import render_template
from flask.views import MethodView
import gbmodel

class Index(MethodView):
    def get(self):
        """
        Redirects to index.html
        """
        model = gbmodel.get_model()
        return render_template('index.html')
