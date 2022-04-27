import json
import requests

def request_to_dict(url) -> dict:
    return json.loads(requests.get(url).text)

def library_search(media_list, search) -> list:
    ret = []
    for i in media_list:
        if i.lower().find(search.lower()) != -1:
            print(i)
            ret.append(i)
    return ret

def build_data(media_list, username) -> str:
    from Tmdb_api import Tmdb_api
    data = ""
    x = Tmdb_api()
    counter = 1
    for m in media_list:
        this = x.search(m)[0]
        data += "<td>" + "<img src=" + this.thumbnail_url + " width=\"200\" height =\"auto\"/></td>"
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