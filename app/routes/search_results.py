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
		data += "<td>" + "" + "</td>"
		data += "<td>" + movie.title + "</td>"
		data += "<td>" + str(movie.rating) + "</td>"
		data += "<td>" + movie.overview + "</td>"
		data += "</tr>"
	data = "<table border = 1>" + data + "</table>"
	return render_template('search_results.html', data=data)