from flask import *
from flask import Flask, request, render_template
from app import app
from Tmdb_api import Tmdb_api
from tinydb import TinyDB, Query, table
from tinydb.operations import add
from tinydb.operations import delete, set
from Util import library_search, build_data, check_status
import requests
import json


counter = 0
db = TinyDB("loginInfo.json")
User = Query()
movie_db = TinyDB("movies.json")
Movie = Query()
res = []
storage = {}
username = ""

@app.route('/search_results', methods=('GET', 'POST'))
def search_results():
	global counter
	global db
	global User
	global res
	global storage
	global username
	search = request.args["query"]
	username = request.args["user"]

	print("user: ", username)
	
	# if not check_status(User, username, db):
	# 	return redirect(url_for('login'))
	x = Tmdb_api()
	movies = x.search(search)
	data = ""
	inlist = {}
	

	# string = (db.get(User.username == username)).get("movies")
	# string = string.split('~~~')


	# for i in range(len(string)):
	# 	inlist[string[i]] = ""
	for movie in movies:
		tmp = x.get_movie(movie.media_id)
		res.append(tmp.media_id)

		if(str(movie.media_id) in storage):
			pass
		else:
			
			storage[str(tmp.media_id)] = {'media_id': str(tmp.media_id), 'title': movie.title,'overview': tmp.overview, 'year': tmp.year, 
			'date': tmp.date, 'rating': tmp.rating, 'thumbnail_url': tmp.thumbnail_url, 'MEDIA_TYPE': tmp.MEDIA_TYPE, 'runtime': tmp.runtime, 
			'language': tmp.language, 'genres': tmp.genres, 'cover_url': tmp.cover_url}
			
		# if not movie_db.search(Movie.movie == (movie.title)):
		# 	new_movie = {"movie": movie.title, "thumbnail_url": movie.thumbnail_url, "overview": movie.overview, "date": movie.date, "rating": movie.rating, "type": movie.MEDIA_TYPE, "id": str(movie.media_id), "rec_final": "", "rec_thumbnail": ""}
		# 	movie_db.insert(new_movie)


		data += "<tr>"
		data += "<td>" + "<img src=" + movie.thumbnail_url + " width=\"120\" height =\"auto\"/></td>"
		data += "<td><font color=\"white\">" + movie.title + " (" + movie.year + ")" "</font></td>"
		data += "<td style=\"text-align: center\" width=\"50\"><font color=\"white\">" + str(movie.rating) + "</font></td>"
		data += "<td><font color=\"white\">" + movie.overview + "</font></td>"
		if movie.title in inlist:
			data += "<form id='myform2' method='post' action='/remove_movie'><td><a class='button1' value=\">" + str(counter) + "\"><button form='myform2' name='remove' type='submit' value='" + str(counter) + "'>-</button></a></td></form>"
		else:
			data += "<form id='myform' method='post' action='/add_movie'><td><a class='button1' value=\">" + str(counter) + "\"><button form='myform' name='add' type='submit' value='" + str(counter) + "'>+</button></a></td></form>"
		data += "</tr>"
		counter+=1
	data = "<table style=\"width:100%\" border=1>" + data + "</table>"
	error = None


	return render_template('search_results.html', user=username, data=data)


@app.route('/search_again', methods=['POST'])
def search_again():
	global db
	global User
	global movie_db
	global Movie
	global username

	if request.form.get('media-type') == "TMDB":
		x = Tmdb_api()
		movies = x.search(request.form['search'])
		if not movies:
			error = 'No movies found'
		return redirect(url_for('search_results', query=request.form['search'], user=username))

	elif request.form.get('media-type') == "Local Library":
		movies = (db.get(User.username == username)).get("movies")
		movies = movies.split('~~~')
		movies.pop()
		movies = library_search(movies, request.form['search'])
		data = build_data(Movie, movies, username, movie_db)
		return render_template('homepage.html', user=username, data=data)
	return redirect(url_for('search_results', query=request.form['search'], user=username))

@app.route('/add_movie', methods=['POST'] )
def add_movie():
	global counter
	global db
	global User
	global Movie
	global movie_db
	global res
	global username
	global storage
	rec_final = ""
	rec_thumbnail = ""
	x = Tmdb_api()
	recs = []
	open = False
	name = ""


	for i in range(counter):
		if str(i) == request.form["add"]:
			print("RES: ", res[i])
			tmp = x.get_movie(res[i])
			info = {'user': username, 'data' : {'media_id': str(tmp.media_id), 'title': tmp.title,'overview': tmp.overview, 'year': tmp.year, 
			'date': tmp.date, 'rating': tmp.rating, 'thumbnail_url': tmp.thumbnail_url, 'MEDIA_TYPE': tmp.MEDIA_TYPE, 'runtime': tmp.runtime, 
			'language': tmp.language, 'genres': tmp.genres, 'cover_url': tmp.cover_url} }
			print(info)
			headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
			response = requests.post("http://db:8000/add_movie", data=json.dumps(info),headers = headers)
			results = response.json()
			print("JSON: ", results)

			app.logger.debug(f'VERIFIED: {results}')
			verified = results.get('Results')
			print(verified)

			# if storage.has_key(res[i]):
			# #movie_db.search(Movie.movie == res[i]):
			# 	mov = movie_db.get(Movie.movie == res[i])
			# 	if mov.get('rec_final') == "":
			# 		open = True
			# 	name = mov.get('movie')
			# 	recs = x.recommend(int(mov.get('id')), str(mov.get('type')))
			# for rec in recs:
			# 	rec_final += rec.title + "~~~"
			# 	rec_thumbnail += rec.thumbnail_url + "~~~"
			# if open:
			# 	movie_db.update(add("rec_final", rec_final), Movie.movie == name)
			# 	movie_db.update(add("rec_thumbnail", rec_thumbnail), Movie.movie == name)
			# db.update(add('movies', res[i]+"~~~"), User.username == username)

			return redirect(url_for('homepage', user=username))
	return redirect(url_for('homepage', user=username))
	

@app.route('/sign_out', methods=['POST'])
def sign_out():
	global db
	global User
	global username
	db.upsert({'status': 'False'}, User.username == username)
	return redirect(url_for('login'))

@app.route('/remove_movie', methods=['POST'])
def remove_movie():
	global counter
	global db
	global User
	global res
	global username
	string = (db.get(User.username == username)).get("movies")
	for i in range(counter):
		if str(i) == request.form["remove"]:
			string = string.replace(res[i] + "~~~", "")
			db.upsert({'movies': string}, User.username == username)
			return redirect(url_for('homepage', user=username))
	return redirect(url_for('homepage', user=username))

@app.route('/goto_library3', methods=['POST'])
def goto_library3():
    global username
    return redirect(url_for('homepage', user=username))
