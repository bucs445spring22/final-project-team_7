from flask import *
from app import app
from Tmdb_api import Tmdb_api
from HtmlBuilder import HtmlBuilder
from MediaBuilder import MediaBuilder
from Util import library_search
import requests

"""
GLOBAL VARIABLES USED: db, movie_db, User, Movie
Reason: Database needs it

Other global variables: username, id
Reason: Passed between post requests to check validity
"""

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
    data = html_builder.build_mediaview(info)
    return render_template('movie_page.html', data=data)

@app.route('/rate', methods=['POST'])
def rate():
    """
    App route for rating movie that user has added
    Returns: redirection to movie page with updated values
    """
    global media_id
    username = session["name"]
    #NOTE if we are able to rate a movie, it's definitely in database
    #if not user_db.search(Rate.movie_id == (id)):
        #new_rating = {"movie_id": id, "rating": rating}
        #user_db.insert(new_rating)
        #user_db.upsert({'rating': rating}, Rate.movie_id == id)
    rating = request.form.get('rating')
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    info = {'username': username, 'media_id': media_id, 'rating': rating}
    requests.post("http://db:8000/rate", data=json.dumps(info), headers=headers)
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
    return redirect(url_for('search_results', query="test", user=username))

@app.route('/search3', methods=['POST'])
def search3():
    """
    App route for searching through movie page
    Returns: redirection to search results of searched movie
    """
    username = session["name"]
    media_builder = MediaBuilder(username)
    media_list = media_builder.build_library()
    html_builder = HtmlBuilder()
    data = html_builder.build_homepage(media_list, username)
    error = None
    if request.method == 'POST':
        if request.form['search']:
            if request.form.get('media-type') == "TMDB":
                x = Tmdb_api()
                media = x.search(request.form['search'])
                if not media:
                    error = 'No movies found'
                    return render_template('homepage.html', user=username, data=error)
                else:
                    return redirect(url_for('search_results', query=request.form['search'], user=username))
            elif request.form.get('media-type') == "Local Library":
                media_list = library_search(media_list, request.form['search'])
                data = html_builder.build_homepage(media_list, username)
                return render_template('homepage.html', user=username, data=data)

@app.route('/goto_library2', methods=['POST'])
def goto_library2():
    """
    App route for going to the homepage through the movie's metadata page
    Returns: redirecting to homepage
    """
    username = session["name"]
    return redirect(url_for('homepage', user=username))
