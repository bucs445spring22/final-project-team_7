import json
import requests
import os

def request_to_dict(url) -> dict:
    """
    Converts request to dictionary
    Parameters: url (str): URL string for website that has json
    Returns: dict: json to dict of json
    """
    return json.loads(requests.get(url).text)

def library_search(media_list, search) -> list:
    """
    Searches media list in your library and returns list of movies user has added
    Parameters: media_list (list): list of medias in user library
                search (str): string that you are searching
    Returns: list: of movies in library
    """
    ret = []
    for i in media_list:
        if i.lower().find(search.lower()) != -1:
            ret.append(i)
    return ret

def build_data(movie_query, media_list, username, db) -> str:
    """
    Builds data for homepage
    Parameters: movie_query (Query): query for movie db
                media_list (list): list of medias
                username (str): username that is logged in
                db (db file): database file of movie
    Returns: str: html that build homepage data
    """
    data = ""
    counter = 1
    id = 0
    for m in media_list:
        if db.search(movie_query.movie == m):
            thumbnail = db.get(movie_query.movie == m)
            id = thumbnail.get("id")
            thumbnail = thumbnail.get("thumbnail_url")
        data += "<form method='post' action='/goto_movie_page'><td><a class='button1' value=\">" + m + "\"><button type='submit' name='mov' value='" + str(id) + "'><img src ='" + thumbnail + "'></button></a></td></form>"
        data += "<td style=color:white width='100'>" + m + "</td>"
        if counter%5 == 0 and counter > 0:
            data+= "<tr></tr>"
        counter+=1
    data = "<table border=1>" + data + "</table>"
    data = "<h1 style=color:white>Welcome to your library, " + username + "!</h1>" + data
    print(data)
    return data

def build_media(movie_query, id, db, rate_query, user_db) -> str:
    from tinydb import TinyDB
    """
    Builds data for individual movie clicked
    Parameters: movie_query (Query): query for movie db
                id (str): string containing movie id
                db (db file): database file of movie
                rate_query(Query): query for rate debug
                user_db (db file): db file of user ratings for movies
    Returns: str: that builds media html
    """
    data = ""
    counter = 0
    avg = 0
    dbfiles = []
    newcount = 0
    if db.search(movie_query.id == id):
        mov = db.get(movie_query.id == id)
        rec_final = mov.get('rec_final').split("~~~")
        rec_thumbnail = mov.get('rec_thumbnail').split("~~~")
        data += "<div style=color:white>"
        data += "<h1 style=color:white>" + mov.get('movie') + " " + mov.get('date') + " (" + str(mov.get('rating')) + ")" "</h1>"
        data += "<img src=" + mov.get('thumbnail_url') + " width=\"350\" height =\"auto\"/>"
        if not user_db.search(rate_query.movie_id == (id)):
            data += "<h2 style=color:white> Your Rating: N/A" + "<form method='post' action='/rate'> <select name='rating' id='rating'></h2>"
            for i in range(11):
                data+="<option value='" + str(i)+ "'>" + str(i) +"</option>"
        else:
            rating = user_db.get(rate_query.movie_id == id)
            rate_value = rating.get('rating')
            data += "<h2 style=color:white> Your Rating: " + str(rate_value) + "<form method='post' action='/rate'> <select name='rating' id='rating'></h2>"
            for i in range(11):
                data+="<option value='" + str(i)+ "'>" + str(i) +"</option>"
            directory_list = os.listdir()
            for file in directory_list:
                filename = os.fsdecode(file)
                if filename.endswith("USERDB.json"):
                    dbfiles.append(filename)
            for filename in dbfiles:
                avgdb = TinyDB(filename)
                if avgdb.search(rate_query.movie_id == (id)):
                    newcount += 1
                    rating2 = avgdb.get(rate_query.movie_id == id)
                    rate_value2 = rating2.get('rating')
                    avg += float(rate_value2)
        if newcount == 0:
            avg = "N/A"
        else:
            avg = avg/newcount
        data+= "</select><button type='submit'>Rate Movie</button></form></p>\n"
        data += "</div>"
        data += "<div style=color:white>" + "<h2 style=color:white> OVERALL USER RATING: " + str(avg) + "</h2>"
        data += "<p style=color:white>" + "[" + mov.get('type') + "] " + mov.get('overview') + "</p></div>"
        data += "<h2 style=color:white>"+ "Because you watched this, here's some related content:" +"</h2>"
        data += "<table border=1>"
        for i in range(len(rec_final)-1):
            data += "<form method='post' action='/search_rec'><td style=color:white width='200'><a class='button1' value=\">" + str(id) + "\"><button type='submit' name='mov' value='" + str(id) + "'>"+ "<img src=" + rec_thumbnail[i] + " width=\"200\" height =\"auto\"/>"
            data += "<p style=color:black>" + rec_final[i] + "</p></td> " + "</button></a></form>"
            counter +=1
            if counter%5==0:
                data+= "<tr></tr>"
        data += "</table>"
        data += "</div>"
    return data

def check_status(User, username, db):
    """
    Checks login status
    Parameters: User (Query): query for user db
                username (str): username of person making request
                db (db): User database to see who's logged in
    Returns: bool indicating a user's login status
    """
    status = ""
    if db.search(User.username == username):
        ret = db.get(User.username == username)
        status = ret.get("status")
    if status == "False":
        return False
    else:
        return True
