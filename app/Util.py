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
            id = thumbnail.get("id")
            thumbnail = thumbnail.get("thumbnail_url")
        data += "<form method='post' action='/goto_movie_page'><td><a class='button1' value=\">" + m + "\"><button type='submit' name='mov' value='" + str(id) + "'><img src ='" + thumbnail + "'></button></a></td></form>"
        #data += "<form id='myform3' method='post' action='/goto_movie_page'><td><input type='image' form ='myform3' name='page' src='" + thumbnail + "' value ='" + m +"' width=\"200\" height =\"auto\"/></td></form>"
        data += "<td style=color:white width='100'>" + m + "</td>"
        if counter%5 == 0 and counter > 0:
            data+= "<tr></tr>"
        counter+=1
    data = "<table border=1>" + data + "</table>"
    data = "<h1 style=color:white>Welcome to your library, " + username + "!</h1>" + data
    return data

def build_media(Movie, id, db) -> str:
    data = ""
    counter = 0
    if db.search(Movie.id == id):
        mov = db.get(Movie.id == id)
        title = mov.get('movie')
        thumbnail = mov.get('thumbnail_url')
        overview = mov.get('overview')
        date = str(mov.get('date'))
        rating = str(mov.get('rating'))
        type = mov.get('type')
        rec_final = mov.get('rec_final')
        rec_thumbnail = mov.get('rec_thumbnail')
        rec_final = rec_final.split("~~~")
        rec_thumbnail = rec_thumbnail.split("~~~")
        data += "<div style=''>"
        data += "<h1 style=color:white>" + title + " " + date + " (" + rating + ")" "</h1>"
        data += "<img src=" + thumbnail + " width=\"350\" height =\"auto\"/>"
        data += "<p style=color:white>" + "[" + type + "] " + overview + "</p>"
        data += "</div>"
        data += "<h2 style=color:white>"+ "Because you watched this, here are some related medias:" +"</h2>"
        data += "<table border=1>"
        for i in range(len(rec_final)-1):
            data += "<td style=color:white width='200'><img src=" + rec_thumbnail[i] + " width=\"200\" height =\"auto\"/>"
            data += "<p style=color:white>" + rec_final[i] + "</p></td>"
            counter +=1
            if counter%7==0:
                data+= "<tr></tr>"
        data += "</table>"
        data += "</div>"
    return data

def check_status(User, username, db):
    status = ""
    
    if db.search(User.username == username):
        ret = db.get(User.username == username)
        status = ret.get("status")
    if status == "False":
        return False
    else:
        return True
