#from Api import Api
from Movie import Movie
import requests
import json

class Tmdb_api:
    API_KEY = "d7dbb644708bdabf2a395267c0890814"

    def __request_to_dict(self, url):
        return json.loads(requests.get(url).text)

    def __thumbnail_gen(self, poster_path):
        return "https://www.themoviedb.org/t/p/w188_and_h282_bestv2" + poster_path

    def __cover_gen(self, poster_path):
        return "https://www.themoviedb.org/t/p/w1280" + poster_path

    def get_movie(self, media_id):
        data = self.request_to_dict("https://api.themoviedb.org/3/movie/" + media_id + "?api_key=" + self.API_KEY)
        movie = Movie(Movie(data.get('id'), data.get('title'), data.get('overview'), data.get('release_date'), data.get('vote_average'), self.__cover_gen(data.get('poster_path'))))
        movie.runtime = data.get('runtime')
        movie.language = data.get('original_language')
        movie.genres = data.get('genres')
        movie.cover_url = self.__cover_gen(data.get('poster_path'))
        return movie

    def get_show(self, media_id):
        pass

    def recommend(self, media_id):
        pass

    def search(self, title):
        title = title.replace(" ", "+")
        movie_data = self.__request_to_dict("https://api.themoviedb.org/3/search/movie?api_key=" + self.API_KEY + "&query=" + title)
        #show_data = self.__request_to_dict("https://api.themoviedb.org/3/search/tv?api_key=" + self.API_KEY + "&query=" + title)
        ret = []
        for i in movie_data.get('results'):
            ret.append(Movie(i.get('id'), i.get('title'), i.get('overview'), i.get('release_date'), i.get('vote_average'), self.__thumbnail_gen(i.get('poster_path'))))
        return ret
