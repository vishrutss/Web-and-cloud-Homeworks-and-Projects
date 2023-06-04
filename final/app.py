import flask
from flask.views import MethodView
from index import Index
from display import Display
from favourites import Favourites
from submit import Submit


app = flask.Flask(__name__)

app.add_url_rule('/',
                 view_func=Index.as_view('index'),
                 methods=["GET"])

app.add_url_rule('/favourites',
                 view_func=Favourites.as_view('favourites'),
                 methods=["GET", "POST"])

app.add_url_rule('/submit',
                 view_func=Submit.as_view('submit'),
                 methods=['POST'])

app.add_url_rule('/display/<int:movie_id>',
                 view_func=Display.as_view('display'),
                 methods=["GET"])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

