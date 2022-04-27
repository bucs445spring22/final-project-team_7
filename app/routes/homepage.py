from flask import *
from app import app
from Tmdb_api import Tmdb_api
from tinydb import TinyDB, Query
import LibrarySearch

@app.route('/homepage', methods=('GET', 'POST'))
def homepage():
    db = TinyDB("loginInfo.json")
    User = Query()
    status = ""
    username = request.args['user']
    movies = (db.get(User.username == username)).get("movies")
    movies = movies.split('**')
    movies.pop()
    data = build_data(movies, username)
    if db.search(User.username == username):
        ret = db.get(User.username == username)
        status = ret.get("status")
    error = None
    if status == "True":
        if request.method == 'POST':
            if request.form['search']:
                if request.form.get('media-type') == "TMDB":
                    x = Tmdb_api()
                    movies = x.search(request.form['search'])
                    if not movies:
                        error = 'No movies found'
                    else:
                        return redirect(url_for('search_results', query=request.form['search'], user=username))
                elif request.form.get('media-type') == "Local Library":
                    movies = library_search(movies, request.form['search'])
                    data = build_data(movies, username)
                    return render_template('homepage.html', error=error, data=data)
    else:
        return redirect(url_for('login'))
    return render_template('homepage.html', error=error, data=data)

def library_search(media_list, search) -> list:
    ret = []
    for i in media_list:
        if i.lower().find(search.lower()) != -1:
            print(i)
            ret.append(i)
    return ret

def build_data(media_list, username) -> str:
    data = ""
    x = Tmdb_api()
    counter = 1
    for m in media_list:
        this = x.search(m)[0]
        data += "<td>" + "<img src=" + this.thumbnail_url + " width=\"200\" height =\"auto\"/></td>"
        data += "<td style=color:white width='100'>" + m + "</td>"
        if counter%5 == 0 and counter > 0:
            data+= "<tr></tr>"
        counter+=1
    data = "<table border=1>" + data + "</table>"
    data = "<h1 style=color:white>Welcome to your library, " + username + "!</h1>" + data
    return data
