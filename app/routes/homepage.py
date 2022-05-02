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

@app.route('/homepage', methods=['GET', 'POST'])
def homepage():
    global db
    global User
    global username
    global Movie
    global movie_db
    username = request.args['user']
    movies = (db.get(User.username == username)).get("movies")
    movies = movies.split('~~~')
    movies.pop()
    data = build_data(Movie, movies, username, movie_db)
    error = None
    status = ""
    if not check_status(User, username, db):
        return redirect(url_for('login'))
    return render_template('homepage.html', error=error, data=data)

@app.route('/search', methods=['POST'])
def search():
    global db
    global User
    global username
    global Movie
    global movie_db
    movies = (db.get(User.username == username)).get("movies")
    movies = movies.split('~~~')
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
                data = build_data(Movie, movies, username, movie_db)
                return render_template('homepage.html', user=username, data=data)

@app.route('/sign_out2', methods=['POST'])
def sign_out2():
    global db
    global User
    global username
    db.upsert({'status': 'False'}, User.username == username)
    return redirect(url_for('login'))

@app.route('/goto_movie_page', methods=['POST'])
def goto_movie_page():
    global username
    return redirect(url_for('movie_page', user=username, id=request.form['mov']))

@app.route('/goto_library', methods=['POST'])
def goto_library():
    global username
    return redirect(url_for('homepage', user=username))
