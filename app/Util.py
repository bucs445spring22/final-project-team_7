import json
import requests

def request_to_dict(url) -> dict:
    return json.loads(requests.get(url).text)

def library_search(media_list, search) -> list:
    ret = []
    for i in media_list:
        if i.lower().find(search.lower()) != -1:
            ret.append(i)
    return ret

def build_data(Movie, media_list, username, db) -> str:
    data = ""
    counter = 1
    for m in media_list:
        if db.search(Movie.movie == m):
            thumbnail = db.get(Movie.movie == m)
            thumbnail = thumbnail.get("thumbnail_url")
        data += "<form method='post' action='/goto_movie_page'><td><a class='button1' value=\">" + m + "\"><button type='submit' value='" + m + "'><img src ='" + thumbnail + "'></button></a></td></form>"
        #data += "<form id='myform3' method='post' action='/goto_movie_page'><td><input type='image' form ='myform3' name='page' src='" + thumbnail + "' value ='" + m +"' width=\"200\" height =\"auto\"/></td></form>"
        data += "<td style=color:white width='100'>" + m + "</td>"
        if counter%5 == 0 and counter > 0:
            data+= "<tr></tr>"
        counter+=1
    data = "<table border=1>" + data + "</table>"
    data = "<h1 style=color:white>Welcome to your library, " + username + "!</h1>" + data
    return data

def check_status(User, username, db):
    if db.search(User.username == username):
        ret = db.get(User.username == username)
        status = ret.get("status")
    if status == "False":
        return False
    else:
        return True
