from flask import Flask , render_template, request
from animesearch import get_results , get_season, get_info_by_id, get_large_image
app = Flask(__name__)


@app.route('/')
def index():

    return render_template("index.html",season = get_season())

@app.route('/info/<int:id>')
def info(id):
    synopsis = get_info_by_id(id)
    im = get_large_image(id)
    print (im)

    return render_template("anime_info.html",synopsis= synopsis)



if __name__ == "__main__":
    app.run(debug=True)

    