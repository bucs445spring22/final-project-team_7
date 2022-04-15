#from Api import Api
from Movie import Movie
from Show import Show
from Season import Season
import requests
import json

class Tmdb_api:
    API_KEY = "d7dbb644708bdabf2a395267c0890814"

    def request_to_dict(self, url) -> dict:
        return json.loads(requests.get(url).text)

    def thumbnail_gen(self, poster_path) -> str:
        if str(poster_path) == "None":
            return "https://blog.springshare.com/wp-content/uploads/2010/02/nc-md.gif"
        return "https://www.themoviedb.org/t/p/w188_and_h282_bestv2" + poster_path

    def cover_gen(self, poster_path) -> str:
        if str(poster_path) == "None":
            return "https://blog.springshare.com/wp-content/uploads/2010/02/nc-md.gif"
        return "https://www.themoviedb.org/t/p/w1280" + poster_path

    def get_movie(self, media_id) -> Movie:
        data = self.request_to_dict("https://api.themoviedb.org/3/movie/" + str(media_id) + "?api_key=" + self.API_KEY)
        movie = Movie(data.get('id'), data.get('name'), data.get('overview'), data.get('release_date'), data.get('vote_average'), self.thumbnail_gen(data.get('poster_path')))
        movie.runtime = data.get('runtime')
        movie.language = data.get('original_language')
        movie.genres = data.get('genres')
        movie.cover_url = self.cover_gen(data.get('poster_path'))
        return movie

    def get_show(self, media_id) -> Show:
        data = self.request_to_dict("https://api.themoviedb.org/3/tv/" + str(media_id) + "?api_key=" + self.API_KEY)
        show = Show(data.get('id'), data.get('title'), data.get('overview'), data.get('first_air_date'), data.get('vote_average'), self.thumbnail_gen(data.get('poster_path')))
        show.runtime = data.get('episode_run_time')[0]
        show.language = data.get('original_language')
        show.genres = data.get('genres')
        show.cover_url = self.cover_gen(data.get('poster_path'))
        show.total_episodes = data.get('number_of_episodes')
        show.total_seasons = data.get('number_of_seasons')
        show.seasons = self.init_season_list(data);
        return show

    def init_season_list(self, data) -> list:
        return [Season(i.get('id'), i.get('name'), i.get('overview'), i.get('episode_count'), i.get('air_date'), self.thumbnail_gen(i.get('poster_path')), self.cover_gen(i.get('poster_path'))) for i in data.get('seasons')]

    def recommend(self, media_id, MEDIA_TYPE) -> list:
        t = "tv/" if MEDIA_TYPE == "Show" else "movie/"
        data = request_to_dict("https://api.themoviedb.org/3/" + t + str(media_id) + "/recommendations?api_key=" + self.API_KEY)
        media_list = []
        if MEDIA_TYPE == "Movie":
            media_list = [Movie(i.get('id'), i.get('title'), i.get('overview'), i.get('release_date'), i.get('vote_average'), self.thumbnail_gen(i.get('poster_path'))) for i in data.get('results')]
        elif MEDIA_TYPE == "Show":
            media_list = [Show(i.get('id'), i.get('name'), i.get('overview'), i.get('first_air_date'), i.get('vote_average'), self.thumbnail_gen(i.get('poster_path'))) for i in data.get('results')]
        return media_list

    def search(self, title) -> list:
        title = title.replace(" ", "+")
        movie_data = self.request_to_dict("https://api.themoviedb.org/3/search/movie?api_key=" + self.API_KEY + "&query=" + title)
        show_data = self.request_to_dict("https://api.themoviedb.org/3/search/tv?api_key=" + self.API_KEY + "&query=" + title)

        movie_list = [Movie(i.get('id'), i.get('title'), i.get('overview'), i.get('release_date'), i.get('vote_average'), self.thumbnail_gen(i.get('poster_path'))) for i in movie_data.get('results')]

        show_list = [Show(i.get('id'), i.get('name'), i.get('overview'), i.get('first_air_date'), i.get('vote_average'), self.thumbnail_gen(i.get('poster_path'))) for i in show_data.get('results')]
        if len(movie_list) == 0:
            return show_list
        if len(show_list) == 0:
            return movie_list
        return [sub[item] for item in range(min(len(movie_list), len(show_list))) for sub in [movie_list, show_list]]
