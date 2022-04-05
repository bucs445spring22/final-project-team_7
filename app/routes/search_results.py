from flask import *
from app import app
from Tmdb_api import Tmdb_api

@app.route('/search_results/<query>', methods=('GET', 'POST'))
def search_results(query):
	x = Tmdb_api()
	movies = x.search(query)
	res = []
	data = ""
	for movie in movies:
		data += "<tr>"
		data += "<td>" + "<img src=" + movie.thumbnail_url + " width=\"120\" height =\"auto\"/></td>"
		data += "<td><font color=\"white\">" + movie.title + " (" + movie.release_date + ")" "</font></td>"
		data += "<td style=\"text-align: center\" width=\"50\"><font color=\"white\">" + str(movie.rating) + "</font></td>"
		data += "<td><font color=\"white\">" + movie.overview + "</font></td>"
		data += "<td><a href=\"something\" class=\"button1\">+</a></td>"
		data += "</tr>"
	data = "<table style=\"width:100%\" border=1>" + data + "</table>"
	error = None
	if request.method == 'POST':
		if request.form['search']:
			x = Tmdb_api()
			movies = x.search(request.form['search'])
			if not movies:
				error = 'No movies found'
			else:
				return redirect(url_for('search_results', query=request.form['search']))
	return render_template('search_results.html', data=data, error=error)
