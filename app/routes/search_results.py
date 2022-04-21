from flask import *
from app import app
from Tmdb_api import Tmdb_api
from tinydb import TinyDB, Query
from tinydb.operations import add

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
	x = Tmdb_api()
	movies = x.search(search)
	data = ""
	inlist = {}
	string = (db.get(User.username == username)).get("movies")
	string = string.split(',')
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
			data += "<td><a class='button1' value=\">" + str(counter) + "\"><button form='myform' name='add' type='submit' value='" + str(counter) + "'>C</button></a></td>"
		else:
			data += "<td><a class='button1' value=\">" + str(counter) + "\"><button form='myform' name='add' type='submit' value='" + str(counter) + "'>+</button></a></td>"
		data += "</tr>"
		counter+=1
	data = "<table style=\"width:100%\" border=1>" + data + "</table>"
	error = None
	return render_template('search_results.html', user=username, data=data)


@app.route('/search_again', methods=['POST'])
def search_again():
	x = Tmdb_api()
	movies = x.search(request.form['search'])
	if not movies:
		error = 'No movies found'
		return render_template('homepage.html', error=error, user=username)
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
			db.update(add('movies', res[i]+","), User.username == username)
			return redirect(url_for('homepage', user=username))
	return redirect(url_for('homepage', user=username))
