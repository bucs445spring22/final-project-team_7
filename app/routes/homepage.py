from flask import *
from app import app
from Tmdb_api import Tmdb_api
from tinydb import TinyDB, Query

@app.route('/homepage', methods=('GET', 'POST'))
def homepage():
    db = TinyDB("loginInfo.json")
    User = Query()
    status = ""
    username = request.args['user']
    if db.search(User.username == username):
        ret = db.get(User.username == username)
        status = ret.get("status")
    error = None
    if status == "True":
        if request.method == 'POST':
            if request.form['search']:
                x = Tmdb_api()
                movies = x.search(request.form['search'])
                if not movies:
                    error = 'No movies found'
                else:
                    return redirect(url_for('search_results', query=request.form['search'], user=username))
    else:
        return redirect(url_for('login'))
    return render_template('homepage.html', error=error)
