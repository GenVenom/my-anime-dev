from flask import Flask , render_template ,redirect,flash
from animesearch import get_results , get_season, get_info_by_id, get_large_image
import sqlite3


app = Flask(__name__)
app.secret_key= "hi"


@app.route('/')
def index():
    
    return render_template("index.html",season = get_season())

@app.route('/info/<int:id>')
def info(id):
    synopsis = get_info_by_id(id)
    img_url = get_large_image(id)
    ctx = {
        'img_url' : img_url,
        'synopsis' : synopsis,
        
    }
    

    return render_template("anime_info.html",context = ctx)

@app.route('/follow/<int:id>')
def follow(id):
    try:
        conn = sqlite3.connect('following.db')
        cursor = conn.cursor()

        conn.execute ("CREATE TABLE IF NOT EXISTS following (anime_id INTEGER PRIMARY KEY)")
        conn.execute("INSERT INTO  following (anime_id) VALUES (?)",(id,))
        conn.commit()
    except:
        flash("You already follow this anime.")

    return redirect("/ ")

if __name__ == "__main__":
    app.run(debug=True)

    