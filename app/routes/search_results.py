from flask import *
from app import app
from Tmdb_api import Tmdb_api
from MediaSerializer import MediaSerializer
from HtmlBuilder import HtmlBuilder
from Util import library_search
import requests
from flask_session import Session
"""
GLOBAL VARIABLES USED: db, movie_db, User, Movie
Reason: Database needs it

Other global variables:
username: Reason: Passed between post requests to check validity
counter: Reason: need to pass counter to other post requests to check which movie is which (there is a better method no time)
res: Reason: need to pass result between different post requests, again definitely another way to do this.
"""
counter = 0
res = []

@app.route('/search_results', methods=('GET', 'POST'))
def search_results():
	"""
    App route for search results page assosciating with searched word
    Returns: template rendering of search results webpage
    """
	global counter
	global res
	username = session["name"]
	search = request.args["query"]
	x = Tmdb_api()
	movies = x.search(search)
	data = ""
	inlist = {}
	if(not movies):
		error = 'No movies found'
		return render_template('homepage.html', user=username, data=error)
	headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
	info = {'username': username}
	inlist = requests.post("http://db:8000/lookup_library", data=json.dumps(info), headers=headers)
	inlist = inlist.json()
	#print(inlist['11'])
	media_ids = []
	for t in inlist.items():
		cur = t[1]
		media_ids.append(cur.get('media_id'))

	for movie in movies:
		res.append(movie.media_id)
		data += "<tr>"
		data += "<td>" + "<img src=" + movie.thumbnail_url + " width=\"120\" height =\"auto\"/></td>"
		data += "<td><font color=\"white\">" + movie.title + " (" + movie.year + ")" "</font></td>"
		data += "<td style=\"text-align: center\" width=\"50\"><font color=\"white\">" + str(movie.rating) + "</font></td>"
		data += "<td><font color=\"white\">" + movie.overview + "</font></td>"
		if movie.media_id in media_ids:
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
	"""
    App route for search results page when you search again in the page assosciating with searched word
    Returns: template rendering of search results webpage
    """
    
	username = session["name"]
	if request.form.get('media-type') == "TMDB":
		x = Tmdb_api()
		movies = x.search(request.form['search'])
		if not movies:
			error = 'No movies found'
		return redirect(url_for('search_results', query=request.form['search'], user=username))
	elif request.form.get('media-type') == "Local Library":
		headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
		info = {'username': username}
		response = requests.post("http://db:8000/lookup_library", data=json.dumps(info), headers=headers)
		media_list = library_search(response, request.form['search'])
		html_builder = HtmlBuilder()
		data = html_builder.build_homepage(media_list, username)
		return render_template('homepage.html', user=username, data=data)
	return redirect(url_for('search_results', query=request.form['search'], user=username))

@app.route('/add_movie', methods=['POST'])
def add_movie():
	"""
    App route for if user has clicked add movie, it will add movie to db and redirect to homepage
    Returns: template rendering of homepage (my library)
    """
	global counter
	global res

	#rec_final = ""
	#rec_thumbnail = ""
	#recs = []
	#open = False
	#name = ""
	#print("counter: ", counter)
	username = session["name"]
	x = Tmdb_api()
	username = session['name']
	for i in range(counter):
		if str(i) == request.form["add"]:
			#print("RES: ", res[i])
			tmp = x.get_movie(res[i])
			media_serializer = MediaSerializer()
			serialized= media_serializer.serialize_media(tmp)
			headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
			data = {'username': username, 'data': serialized}
			#print(info)
			response = requests.post("http://db:8000/add_media", data=json.dumps(data),headers = headers)
			return redirect(url_for('homepage', user=username))
	return redirect(url_for('homepage', user=username))

@app.route('/sign_out', methods=['POST'])
def sign_out():
	"""
    App route for if user has clicked sign out button and signs them out of db.
    Returns: redirection to login page
    """
	session["name"] = None
	return redirect(url_for('login'))

@app.route('/remove_movie', methods=['POST'])
def remove_movie():
	"""
	App route for if user has clicked remove movie, it will remove movie to db and redirect to homepage
	Returns: template rendering of homepage (my library)
	"""
	global counter
	#global db
	#global User
	global res
	#print("HELLO FROM remove_movie")
	media_id = 0
	username = session["name"]
	headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
	for i in range(counter):
		if str(i) == request.form["remove"]:
			media_id = res[i]
			data = {'username': username, 'media_id': media_id}
			requests.post("http://db:8000/remove_media", data=json.dumps(data), headers=headers)
	return redirect(url_for('homepage', user=username))
	#string = (db.get(User.username == username)).get("movies")
	#for i in range(counter):
	#	if str(i) == request.form["remove"]:
	#		string = string.replace(res[i] + "~~~", "")
	#		db.upsert({'movies': string}, User.username == username)
	#		return redirect(url_for('homepage', user=username))

@app.route('/goto_library3', methods=['POST'])
def goto_library3():
	"""
	App route for going back to user library.
	Returns: template rendering of homepage
	"""
	username = session["name"]
	return redirect(url_for('homepage', user=username))
