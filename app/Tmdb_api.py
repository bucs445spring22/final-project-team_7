from Api import Api
from Movie import Movie
import requests
import json

class Tmdb_api(Api):
    API_KEY = "d7dbb644708bdabf2a395267c0890814"
    COVER_URL = "https://www.themoviedb.org/t/p/w1280"

    def get_movie(self, media_id):
        pass

    def get_show(self, media_id):
        pass

    def recommend(self, media_id):
        pass

    # TODO: add search results for shows as well
    def search(self, title):
        title = title.replace(" ", "+")
        movie_req = requests.get("https://api.themoviedb.org/3/search/movie?api_key=" + self.API_KEY + "&query=" + title)
        #show_req = requests.get("https://api.themoviedb.org/3/search/tv?api_key=" + self.API_KEY + "&query=" + title)
        movie_data = json.loads(movie_req.text)
        #show_data = json.loads(show_req.text)
        ret = []
        for i in movie_data.get('results'):
            ret.append(Movie(i.get('genre_ids'), i.get('id'), i.get('title'), i.get('overview'), 
                i.get('poster_path'), i.get('release_date'), i.get('vote_average')))
        return ret
