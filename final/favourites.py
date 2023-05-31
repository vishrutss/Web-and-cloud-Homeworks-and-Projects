"""
Display function
"""
from flask import render_template
from flask.views import MethodView
import gbmodel

class Display(MethodView):
    def get(self):
        """
        Displays the entries from the db file
        """
        model = gbmodel.get_model()
        entries = [dict(bname=row[0], bcode=row[1], floor=row[2], room_num=row[3], rating=row[4] ) for row in model.select()]
        return render_template('display.html',entries=entries)

