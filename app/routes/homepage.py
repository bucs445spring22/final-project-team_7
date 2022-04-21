from flask import *
from app import app
from Tmdb_api import Tmdb_api
from tinydb import TinyDB, Query

@app.route('/homepage', methods=('GET', 'POST'))
def homepage():
    db = TinyDB("loginInfo.json")
    User = Query()
    status = ""
    data = ""
    username = request.args['user']
    movies = (db.get(User.username == username)).get("movies")
    movies = movies.split(',')
    movies.pop()
    for movie in movies:
        data += "<tr style='height:2px'>"
        data += "<td>" + movie + "</td>"
        data += "</tr>"
    data = "<table style=\"width:100%\" border=1>" + data + "</table>"
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
    return render_template('homepage.html', error=error, data=data)
