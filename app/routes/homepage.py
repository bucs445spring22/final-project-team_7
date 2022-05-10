from flask import *
from app import app
from Tmdb_api import Tmdb_api
#from tinydb import TinyDB, Query
from MediaBuilder import MediaBuilder
from HtmlBuilder import HtmlBuilder
from Util import library_search, build_data, check_status
import requests
import json

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
username = ""

@app.route('/homepage', methods=['GET', 'POST'])
def homepage():
    """
    App route for homepage (my library)
    Returns: rendering of homepage.html with data
    """
    global username
    username = request.args['user']
    media_builder = MediaBuilder(username)
    media_list = media_builder.build_library()
    html_builder = HtmlBuilder()
    data = html_builder.build_homepage(media_list, username)
    #print(username)
    #data = build_data(Movie, movies, username, movie_db)
    error = None
    status = ""

    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    data = {'username': username}
    verify = requests.post("http://db:8000/checkStatus", data=json.dumps(data), headers=headers)
    #print("\nDEBUG: " + str(verify.json().get('user')))
    #if verify.json().get('user'):
    if not verify.json().get('user'):
        return redirect(url_for('login'))
    return render_template('homepage.html', error=error, data=data)

@app.route('/search', methods=['POST'])
def search():
    """
    App route for search (my library)
    Returns: rendering of search results either in search_results or homepage depending on button selected
    """
    global username
    username = request.args['user']
    media_builder = MediaBuilder(username)
    media_list = media_builder.build_library()
    html_builder = HtmlBuilder()
    data = html_builder.build_homepage(media_list, username)
    #data = build_data(Movie, movies, username, movie_db)
    error = None
    if request.method == 'POST':
        if request.form['search']:
            if request.form.get('media-type') == "TMDB":
                x = Tmdb_api()
                media = x.search(request.form['search'])
                if not media:
                    error = 'No movies found'
                else:
                    return redirect(url_for('search_results', query=request.form['search'], user=username))
            elif request.form.get('media-type') == "Local Library":
                media_list = library_search(media_list, request.form['search'])
                #data = build_data(Movie, movies, username, movie_db)
                data = html_builder.build_homepage(media_list, username)
                return render_template('homepage.html', user=username, data=data)

@app.route('/sign_out2', methods=['POST'])
def sign_out2():
    """
    App route for sign out
    Returns: rendering of search results either in search_results or homepage depending on button selected
    """
    global username
    #db.upsert({'status': 'False'}, User.username == username)
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    data = {'username': username}
    requests.post("http://db:8000/logout", data=json.dumps(data), headers=headers)
    return redirect(url_for('login'))

@app.route('/goto_movie_page', methods=['POST'])
def goto_movie_page():
    """
    App route for movie metadata page
    Returns: redirect for individual movie page
    """
    global username
    return redirect(url_for('movie_page', user=username, id=request.form['mov']))

@app.route('/goto_library', methods=['POST'])
def goto_library():
    """
    App route for library through library
    Returns: redirects to homepage
    """
    global username
    return redirect(url_for('homepage', user=username))
