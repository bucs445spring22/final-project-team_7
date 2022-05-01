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

@app.route('/movie_page', methods=['GET','POST'])
def movie_page():
    return render_template('movie_page.html', user=username)
