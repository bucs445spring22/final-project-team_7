from flask import *
from app import app
from Tmdb_api import Tmdb_api
from HtmlBuilder import HtmlBuilder
from MediaBuilder import MediaBuilder
#from tinydb import TinyDB, Query
from Util import library_search, build_data, check_status, build_media
import requests

"""
GLOBAL VARIABLES USED: db, movie_db, User, Movie
Reason: Database needs it

Other global variables: username, id
Reason: Passed between post requests to check validity
"""

#db = TinyDB("login_info.json")
#movie_db = TinyDB("movies.json")
#User = Query()
#Movie = Query()
username = ""
media_id = ""

@app.route('/movie_page', methods=['GET','POST'])
def movie_page():
    """
    App route for page of each movie
    Returns: rendering of movie.html with data
    """
    username = session["name"]
    global media_id
    username = request.args['user']
    media_id = request.args['id']

    media_builder = MediaBuilder(username)
    info = media_builder.build_media(media_id)
    html_builder = HtmlBuilder()
    html_builder.build_mediaview(info)
    return render_template('movie_page.html', data=info)

@app.route('/rate', methods=['POST'])
def rate():
    """
    App route for rating movie that user has added
    Returns: redirection to movie page with updated values
    """
    global media_id
    #Rate = Query()
    #db_str = username+"USERDB.json"
    #user_db = TinyDB(db_str)
    rating = request.form.get('rating')
    if not user_db.search(Rate.movie_id == (id)):
        new_rating = {"movie_id": id, "rating": rating}
        user_db.insert(new_rating)
    else:
        user_db.upsert({'rating': rating}, Rate.movie_id == id)
    return redirect(url_for('homepage', user=username))


@app.route('/sign_out3', methods=['POST'])
def sign_out3():
    
    """
    App route for signing out each user and signs out user once button clicked
    Returns: redirection to login
    """
    session["name"] = None
    return redirect(url_for('login'))

@app.route('/search_rec', methods=['POST'])
def search_rec():
    """
    App route for searching rec in movie page
    Returns: redirection to search results of searched movie
    """
    username = session["name"]
    error = None
    return redirect(url_for('search_results', query="test", user=username))

@app.route('/search3', methods=['POST'])
def search3():
    """
    App route for searching through movie page
    Returns: redirection to search results of searched movie
    """
    global db
    global User
    username = session["name"]
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

@app.route('/goto_library2', methods=['POST'])
def goto_library2():
    """
    App route for going to the homepage through the movie's metadata page
    Returns: redirecting to homepage
    """
    username = session["name"]
    return redirect(url_for('homepage', user=username))
