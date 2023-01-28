from flask import Flask , render_template ,redirect,request , url_for,abort
import sqlite3
from gogoscraper import get_stream_url , get_search_results ,get_home_page ,get_anime_info

app = Flask(__name__)


conn = sqlite3.connect('following.db')
c = conn.cursor()

c.execute ("CREATE TABLE IF NOT EXISTS following (anime_name STRING)")
conn.commit()
conn.close()

@app.route('/',methods=['GET','POST'])
def index():
    if request.method == "GET":
        following_list = []
        conn= sqlite3.connect('following.db')
        c= conn.cursor()

        c.execute("SELECT * from following")
        data = c.fetchall()
        conn.close()
        for i in data:
            following_list.append(i[0])

        
        ctx = {
            "season" : get_home_page(),
            "following_list" : following_list
        }
        return render_template("index.html",context=ctx)
    else:
        query = request.form['search-query']
        return redirect (url_for('search',query = query))

# FIX URL NAME NOT CHANGING WHEN SEARCHED FROM SEARCH PAGE!
@app.route('/search/<string:query>',methods=['GET','POST'])
def search(query):
    if request.method != "GET":
        query = request.form['search-query']
    
   
    results = get_search_results(query)
    if not results:
        abort(404)   
    return render_template("search.html",results = results,search_name = query)
        
@app.route('/info/<string:name>',methods=['GET','POST'])
def info(name):
    name = name.strip()
    if request.method !="POST":
        try:
            ctx = get_anime_info(name)
            return render_template("anime_info.html",context = ctx)
        except AttributeError:
            abort(404)
    else:
        query = request.form['search-query']
        return redirect (url_for('search',query = query))
        

@app.route('/follow/<string:name>')
def follow(name):
    
    try:
        conn = sqlite3.connect('following.db')
        c = conn.cursor()

        c.execute ("CREATE TABLE IF NOT EXISTS following (anime_name STRING)")
        c.execute("INSERT INTO  following (anime_name) VALUES (?)",(name,))
        conn.commit()
        conn.close()
    except Exception as e:
        print(e)
        
        pass

    return redirect(f"/#{name}")

@app.route('/unfollow/<string:name>')
def unfollow(name):
    
    conn= sqlite3.connect('following.db')
    c = conn.cursor()
    c.execute("DELETE FROM following WHERE anime_name = ?",(name,))
    conn.commit()
    conn.close()
    return redirect(f"/#{name}")

@app.route('/video/<string:anime_name>/<int:ep_id>',methods=['GET','POST'])
def video(anime_name , ep_id):
    
    if request.method != "POST":
        video_url,episodes = get_stream_url(anime_name, ep_id)
        
        context = {
            'video_feed':video_url,
            'anime_name': anime_name,
            'ep_id':ep_id,
            'episodes' : episodes
        }
        return render_template("video_player.html",context=context)
    else:
        query = request.form['search-query']
        
        return redirect (url_for('search',query = query))

@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(debug=True)


