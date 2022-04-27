from flask import *
from app import app
from Tmdb_api import Tmdb_api
from tinydb import TinyDB, Query
from tinydb.operations import add
from tinydb.operations import delete, set
from Util import library_search, build_data, check_status

counter = 0
db = TinyDB("loginInfo.json")
User = Query()
res = []
username = ""

@app.route('/search_results', methods=('GET', 'POST'))
def search_results():
	global counter
	global db
	global User
	global res
	global username
	search = request.args["query"]
	username = request.args["user"]
	if not check_status(User, username, db):
		return redirect(url_for('login'))
	x = Tmdb_api()
	movies = x.search(search)
	data = ""
	inlist = {}
	string = (db.get(User.username == username)).get("movies")
	string = string.split('**')
	for i in range(len(string)):
		inlist[string[i]] = ""
	for movie in movies:
		res.append(movie.title)
		data += "<tr>"
		data += "<td>" + "<img src=" + movie.thumbnail_url + " width=\"120\" height =\"auto\"/></td>"
		data += "<td><font color=\"white\">" + movie.title + " (" + movie.year + ")" "</font></td>"
		data += "<td style=\"text-align: center\" width=\"50\"><font color=\"white\">" + str(movie.rating) + "</font></td>"
		data += "<td><font color=\"white\">" + movie.overview + "</font></td>"
		if movie.title in inlist:
			data += "<td><a class='button1' value=\">" + str(counter) + "\"><button form='myform' name='remove' type='submit' value='" + str(counter) + "'>-</button></a></td>"
		else:
			data += "<td><a class='button1' value=\">" + str(counter) + "\"><button form='myform' name='add' type='submit' value='" + str(counter) + "'>+</button></a></td>"
		data += "</tr>"
		counter+=1
	data = "<table style=\"width:100%\" border=1>" + data + "</table>"
	error = None
	return render_template('search_results.html', user=username, data=data)


@app.route('/search_again', methods=['POST'])
def search_again():
	global db
	global User
	if request.form.get('media-type') == "TMDB":
		x = Tmdb_api()
		movies = x.search(request.form['search'])
		if not movies:
			error = 'No movies found'
		return redirect(url_for('search_results', query=request.form['search'], user=username))
	elif request.form.get('media-type') == "Local Library":
		movies = (db.get(User.username == username)).get("movies")
		movies = movies.split('**')
		movies.pop()
		movies = library_search(movies, request.form['search'])
		data = build_data(movies, username)
		return render_template('homepage.html', user=username, data=data)
	return redirect(url_for('search_results', query=request.form['search'], user=username))

@app.route('/add_movie', methods=['POST'])
def add_movie():
	global counter
	global db
	global User
	global res
	global username
	for i in range(counter):
		if str(i) == request.form["add"]:
			db.update(add('movies', res[i]+"**"), User.username == username)
			return redirect(url_for('homepage', user=username))
	return redirect(url_for('homepage', user=username))

@app.route('/sign_out', methods=['POST'])
def sign_out():
	global db
	global User
	global username
	db.upsert({'status': 'False'}, User.username == username)
	return redirect(url_for('login'))