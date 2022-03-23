from flask import *
from app import app
from Tmdb_api import Tmdb_api

@app.route('/search_results/<query>', methods=('GET', 'POST'))
def search_results(query):
	x = Tmdb_api()
	movies = x.search(query)
	res = []
	for movie in movies:
		res.append(movie.title)
	return jsonify(res)