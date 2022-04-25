from flask import *
from app import app
from Tmdb_api import Tmdb_api
from tinydb import TinyDB, Query
import LibrarySearch

@app.route('/homepage', methods=('GET', 'POST'))
def homepage():
    counter = 1
    db = TinyDB("loginInfo.json")
    User = Query()
    status = ""
    data = ""
    x = Tmdb_api()
    username = request.args['user']
    movies = (db.get(User.username == username)).get("movies")
    movies = movies.split('**')
    movies.pop()
    for movie in movies:
        this = x.search(movie)[0]
        data += "<td>" + "<img src=" + this.thumbnail_url + " width=\"200\" height =\"auto\"/></td>"
        data += "<td style=color:white width='100'>" + movie + "</td>"
        if counter%5 == 0 and counter > 0:
            data+= "<tr></tr>"
        counter+=1
    data = "<table border=1>" + data + "</table>"
    data = "<h1 style=color:white>Welcome to your library, " + username + "!</h1>" + data
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
