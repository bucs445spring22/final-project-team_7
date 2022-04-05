#from Api import Api
from Movie import Movie
import requests
import json

class Tmdb_api:
    API_KEY = "d7dbb644708bdabf2a395267c0890814"

    def request_to_dict(self, url):
        return json.loads(requests.get(url).text)

    def thumbnail_gen(self, poster_path):
        if str(poster_path) == "None":
            return "https://blog.springshare.com/wp-content/uploads/2010/02/nc-md.gif"
        return "https://www.themoviedb.org/t/p/w188_and_h282_bestv2" + poster_path

    def cover_gen(self, poster_path):
        if str(poster_path) == "None":
            return "https://blog.springshare.com/wp-content/uploads/2010/02/nc-md.gif"
        return "https://www.themoviedb.org/t/p/w1280" + poster_path

    def date_gen(self, date):
        #YYYY-MM-DD to YYYY
        return date[0:4]

    def get_movie(self, media_id):
        data = self.request_to_dict("https://api.themoviedb.org/3/movie/" + str(media_id) + "?api_key=" + self.API_KEY)
        movie = Movie(data.get('id'), data.get('title'), data.get('overview'), self.date_gen(data.get('release_date')), data.get('vote_average'), self.thumbnail_gen(data.get('poster_path')))
        movie.runtime = data.get('runtime')
        movie.language = data.get('original_language')
        movie.genres = data.get('genres')
        movie.cover_url = self.cover_gen(data.get('poster_path'))
        return movie

    def get_show(self, media_id):
        pass

    def recommend(self, media_id):
        pass

    def search(self, title):
        title = title.replace(" ", "+")
        movie_data = self.request_to_dict("https://api.themoviedb.org/3/search/movie?api_key=" + self.API_KEY + "&query=" + title)
        #show_data = self.request_to_dict("https://api.themoviedb.org/3/search/tv?api_key=" + self.API_KEY + "&query=" + title)
        ret = []
        for i in movie_data.get('results'):
            ret.append(Movie(i.get('id'), i.get('title'), i.get('overview'), self.date_gen(i.get('release_date')), i.get('vote_average'), self.thumbnail_gen(i.get('poster_path'))))
        return ret
