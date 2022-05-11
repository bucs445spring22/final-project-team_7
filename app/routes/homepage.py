from flask import *
from app import app
from Tmdb_api import Tmdb_api
#from tinydb import TinyDB, Query
from MediaBuilder import MediaBuilder
from HtmlBuilder import HtmlBuilder
from Util import library_search
import requests
import json
from flask_session import Session

"""
GLOBAL VARIABLES USED: db, movie_db, User, Movie
Reason: Database needs it (I'm not sure initializing db every time would be a good idea either)

Other global variables: username
Reason: Passed between post requests to check validity
"""
#db = TinyDB("login_info.json")
#movie_db = TinyDB("movies.json")
#User = Query()
#Movie = Query()

@app.route('/homepage', methods=['GET', 'POST'])
def homepage():
    """
    App route for homepage (my library)
    Returns: rendering of homepage.html with data
    """
    username = session["name"]
    media_builder = MediaBuilder(username)
    media_list = media_builder.build_library()
    html_builder = HtmlBuilder()
    data = html_builder.build_homepage(media_list, username)
    error = None

    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    info = {'username': username}
    verify = requests.post("http://db:8000/checkStatus", data=json.dumps(info), headers=headers)
    #print("\nDEBUG: " + str(verify.json().get('user')))
    if not verify.json().get('user'):
        return redirect(url_for('login'))
    return render_template('homepage.html', error=error, data=data)

@app.route('/search', methods=['POST'])
def search():
    """
    App route for search (my library)
    Returns: rendering of search results either in search_results or homepage depending on button selected
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

@app.route('/sign_out2', methods=['POST'])
def sign_out2():
    """
    App route for sign out
    Returns: rendering of search results either in search_results or homepage depending on button selected
    """
    session["name"] = None
    return redirect(url_for('login'))

@app.route('/goto_movie_page', methods=['POST'])
def goto_movie_page():
    """
    App route for movie metadata page
    Returns: redirect for individual movie page
    """
    username = session["name"]
    return redirect(url_for('movie_page', user=username, id=request.form['mov']))

@app.route('/goto_library', methods=['POST'])
def goto_library():
    """
    App route for library through library
    Returns: redirects to homepage
    """
    username = session["name"]
    return redirect(url_for('homepage', user=username))
