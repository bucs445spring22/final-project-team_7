from Api import Api

from tmdbv3api import Movie, TMDb

class Tmdb_api(Api):
    API_KEY = "d7dbb644708bdabf2a395267c0890814"
    LANGUAGE = "en-US"
    COVER_URL = "https://www.themoviedb.org/t/p/w1280"
    def __init__(self):
        pass
    def get_movie(self, media_id):
        movie = Movie()
        m = movie.details(media_id)
        cover = COVER_URL + m.poster_path
        pass # should return a Movie?
    def get_show(self, media_id):
        pass
    def recommend(self, media_id):
        pass
    def search_by_id(self, media_id):
        pass
    def search_by_title(self, title):
        pass
