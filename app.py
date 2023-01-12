from flask import Flask , render_template, request
from animesearch import get_results , get_season
app = Flask(__name__)


@app.route('/')
def index():

    return render_template("index.html",season = get_season())

if __name__ == "__main__":
    app.run(debug=True)

    