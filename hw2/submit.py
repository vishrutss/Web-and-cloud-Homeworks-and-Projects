from flask import redirect, request, url_for, render_template
from flask.views import MethodView
import gbmodel

class Submit(MethodView):
    def get(self):
        return render_template('submit.html')

    def post(self):
        """
        Accepts POST requests, and processes the form;
        Redirect to index when completed.
        """
        model = gbmodel.get_model()
        model.insert(request.form['bname'], request.form['bcode'], request.form['floor'], request.form['room_num'], request.form['rating'])
        return redirect(url_for('index'))
