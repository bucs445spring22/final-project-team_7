from Tmdb_api import Tmdb_api

class HtmlBuilder:
    #NOTE HtmlBuilder is to be used after communication with the database is properly working, should replace Util.py build functions
    def build_homepage(self, media_list, username) -> str:
        """
        Builds data to display on homepage
        Parameters: media_list (list): list of media in user's library
                    username (str): username of logged in user
        Returns: A string containing html code of homepage
        """
        data = "<h1 style=color:white>Welcome to your library, " + username + "!</h1><table border=1>"
        counter = 1
        for m in media_list:
            #print("DEBUG " + str(m.media_id))
            if m.media_id == -1:
                break
            data += "<form method='post' action='/goto_movie_page'><td><a class='button1' value=\">" + m.title + "\"><button type='submit' name='mov' value='" + str(m.media_id) + "'><img src ='" + m.thumbnail_url + "'></button></a></td></form>"
            data += "<td style=color:white width='100'>" + m.title + "</td>"
            if counter%5 == 0 and counter > 0:
                data += "<tr></tr>"
            counter += 1
        data += "</table>"
        return data
    def build_mediaview(self, media) -> str:
        """
        Builds webpage to view an individual MediaEntry
        Parameters: media is the Movie or Show object to display
        Returns: A string containing html code of the webpage
        """
        data = ""
        counter = 0
        api = Tmdb_api()
        recommended = api.recommend(media.media_id, media.MEDIA_TYPE)
        #Cover + metadata
        data += "<div style=''><h1 style=color:white>" + media.title + " " + media.date + " (" + str(media.rating) + ")</h1>"
        data += "<img src=" + media.thumbnail_url + " width=\"350\" height =\"auto\"/>"
        #Ratings
        data += "<h2 style=color:white> Your Rating: "
        data += "N/A" if media.user_rating == 0 else str(media.user_rating)
        data += "</h2><form method='post' action='/rate'> <select name='rating' id='rating'></h2><option value='0'></option>"
        for i in range(10): #numbers 1-10, rating 0 means rating isn't set yet
            data += "<option value='" + str(i+1) + "'>" + str(i+1) + "</option>"
        data += "</select><button type='submit'>Rate Movie</button></form>"
        #Overview
        data += "<p style=color:white>" + "[" + media.MEDIA_TYPE + "] " + media.overview + "</p></div>"
        #Recommendations
        if len(recommended) != 0:
            data += "<h2 style=color:white>"+ "Because you watched this, here's some related content:" +"</h2>"
            data += "<table border=1>"
        for i in recommended:
            data += "<td style=color:white width='200'><img src=" + i.thumbnail_url + " width=\"200\" height =\"auto\"/>"
            data += "<p style=color:white>" + i.title + "</p></td>"
            counter +=1
            if counter%7==0:
                data+= "<tr></tr>"
        data += "</table></div>"
        return data