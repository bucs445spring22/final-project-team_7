from flask import *
from app import app
from Tmdb_api import Tmdb_api

@app.route('/homepage', methods=('GET', 'POST'))
def homepage():
    error = None
    if request.method == 'POST':
        if request.form['search']:
            x = Tmdb_api()
            movies = x.search(request.form['search'])
            if not movies:
                error = 'No movies found'
            else:
                return redirect(url_for('search_results', query=request.form['search']))
    return render_template('homepage.html', error=error)