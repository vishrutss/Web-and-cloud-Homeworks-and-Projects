"""
A simple study space location entry flask app.
"""
import flask
from flask.views import MethodView
from index import Index
from submit import Submit
from display import Display

app = flask.Flask(__name__)       # our Flask app

app.add_url_rule('/',
                 view_func=Index.as_view('index'),
                 methods=["GET"])

app.add_url_rule('/submit',
                 view_func=Submit.as_view('submit'),
                 methods=['GET', 'POST'])

app.add_url_rule('/display',
                 view_func=Display.as_view('display'),
                 methods=["GET"])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
