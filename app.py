from flask import Flask , render_template ,redirect,flash
from animesearch import get_results , get_season, get_info_by_id, get_large_image
import sqlite3


app = Flask(__name__)
app.secret_key= "hi"


@app.route('/')
def index():
    following_list = []
    conn= sqlite3.connect('following.db')
    c= conn.cursor()

    c.execute("SELECT * from following")
    data = c.fetchall()
    conn.close()
    for i in data:
        following_list.append(i[0])

    ctx = {
        "season" : get_season(),
        "following_list" : following_list
    }
    return render_template("index.html",context=ctx)

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
        c = conn.cursor()

        c.execute ("CREATE TABLE IF NOT EXISTS following (anime_id INTEGER PRIMARY KEY)")
        c.execute("INSERT INTO  following (anime_id) VALUES (?)",(id,))
        conn.commit()
        conn.close()
    except:
        flash("You already follow this anime.")

    return redirect(f"/#{id}")

@app.route('/unfollow/<int:id>')
def unfollow(id):
    conn= sqlite3.connect('following.db')
    c = conn.cursor()
    c.execute("DELETE FROM following WHERE anime_id = ?",(id,))
    conn.commit()
    conn.close()
    return redirect(f"/#{id}")
if __name__ == "__main__":
    app.run(debug=True)

    