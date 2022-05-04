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
            data += "<form method='post' action='/goto_movie_page'><td><a class='button1' value=\">" + m.get('title') + "\"><button type='submit' name='mov' value='" + str(m.get('media_id')) + "'><img src ='" + m.get('thumbnail_url') + "'></button></a></td></form>"
            data += "<td style=color:white width='100'>" + m.get('title') + "</td>"
            if counter%5 == 0 and counter > 0:
                data += "<tr></tr>"
            counter += 1
        data += "</table>"
        return data
    def build_media(self, media) -> str:
        """
        Builds data for an individual MediaEntry clicked
        Parameters: media is the Movie or Show object to display
        Returns: A string containing html code of the webpage
        """
        #TODO remove call of recommend in search_results.py, recommend will be called here instead
        data = ""
        counter = 0
        api = Tmdb_api()
        recommended = api.recommend(media.media_id, media.MEDIA_TYPE)
        data += "<div style=''><h1 style=color:white>" + media.title + " " + media.date + " (" + str(media.rating) + ")</h1>"
        data += "<img src=" + media.thumbnail_url + " width=\"350\" height =\"auto\"/>"
        data += "<p style=color:white>" + "[" + media.MEDIA_TYPE + "] " + media.overview + "</p></div>"
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
