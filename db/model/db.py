from tinydb import TinyDB, Query
import bcrypt
from tinydb.operations import set

class Database:
    def __init__(self, username = ""):
        self.username = username
        string = username + "_DB.json"
        self.db = TinyDB(string)

    def lookup_library(self):
        que = Query()
        data = ""
        counter = 1
        for m in media_list:
            if self.db.search(Movie.movie == m):
                thumbnail = self.db.get(Movie.movie == m)
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