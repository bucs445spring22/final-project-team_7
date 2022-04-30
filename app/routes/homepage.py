from flask import *
from app import app
from Tmdb_api import Tmdb_api
from tinydb import TinyDB, Query
from Util import library_search, build_data, check_status

db = TinyDB("loginInfo.json")
movie_db = TinyDB("movies.json")
User = Query()
Movie = Query()
username = ""

@app.route('/homepage', methods=('GET', 'POST'))
def homepage():
    global db
    global User
    global username
    status = ""
    username = request.args['user']
    if not check_status(User, username, db):
        return redirect(url_for('login'))
    movies = (db.get(User.username == username)).get("movies")
    movies = movies.split('**')
    movies.pop()
    data = build_data(Movie, movies, username, movie_db)
    error = None
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
                return render_template('homepage.html', user=username, data=data)
    return render_template('homepage.html', error=error, data=data)

@app.route('/sign_out2', methods=['POST'])
def sign_out2():
    global db
    global User
    global username
    db.upsert({'status': 'False'}, User.username == username)
    return redirect(url_for('login'))
