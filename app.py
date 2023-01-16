from flask import Flask , render_template ,redirect,flash,Response
from animesearch import get_results , get_season, get_info_by_id, get_large_image,get_episodes
import sqlite3
import requests
from gogoscraper import get_stream_url
app = Flask(__name__)



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
        'episodes': get_episodes(id),
        'anime_id': id
        
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
        pass

    return redirect(f"/#{id}")

@app.route('/unfollow/<int:id>')
def unfollow(id):
    conn= sqlite3.connect('following.db')
    c = conn.cursor()
    c.execute("DELETE FROM following WHERE anime_id = ?",(id,))
    conn.commit()
    conn.close()
    return redirect(f"/#{id}")

@app.route('/video/<int:anime_id>/<int:ep_id>/')
async def video(anime_id , ep_id):
    video_url = await get_stream_url(anime_id , ep_id)
    print(video_url)
    return render_template("video_player.html",video_feed= video_url)


if __name__ == "__main__":
    app.run(debug=True,port=8000)


