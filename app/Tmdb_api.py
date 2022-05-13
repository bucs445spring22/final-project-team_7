from Api import Api
from Movie import Movie
from Show import Show
from Season import Season
from Util import request_to_dict

class Tmdb_api(Api):
    API_KEY = "d7dbb644708bdabf2a395267c0890814"

    def thumbnail_gen(self, poster_path) -> str:
        """
        Generates the thumbnail url for a given poster path
        Parameters: poster_path(str): poster path as a string
        Returns: string containing the fully generated path to thumbnail url
        """
        if str(poster_path) == "None":
            return "static/cover_not_found.gif"
        return "https://www.themoviedb.org/t/p/w188_and_h282_bestv2" + poster_path

    def cover_gen(self, poster_path) -> str:
        """
        Generates the cover url for a given poster path
        Parameters: poster_path(str): poster path as a string
        Returns: string containing the fully generated path to thumbnail url
        """
        if str(poster_path) == "None":
            return "static/cover_not_found.gif"
        return "https://www.themoviedb.org/t/p/w1280" + poster_path

    def get_movie(self, media_id): #-> Movie:
        """
        Fetches movie from TMDB given a media_id, initializing fields of movie class to the data from the dict
        Parameters: media_id(int): media id corresponding to a particular movie in the API
        Returns: A movie object containing a complete copy of the movie metadata corresponding to the media_id
        """
        data = request_to_dict("https://api.themoviedb.org/3/movie/" + str(media_id) + "?api_key=" + self.API_KEY)
        if 'success' in data:
            tmp = Movie(media_id, 'Invalid', 'Invalid', 'Invalid', 0, "static/cover_not_found.gif")
            tmp.cover_url = "static/cover_not_found.gif"
            return tmp
        movie = Movie(data.get('id'), data.get('title'), data.get('overview'), data.get('release_date'), data.get('vote_average'), self.thumbnail_gen(data.get('poster_path')))
        movie.runtime = data.get('runtime')
        movie.language = data.get('original_language')
        movie.genres = data.get('genres')
        movie.cover_url = self.cover_gen(data.get('poster_path'))
        return movie

    def get_show(self, media_id) -> Show:
        """
        Fetches show from TMDB given a media_id, initializing fields of show class to the data from the dict
        Parameters: media_id(int): media id corresponding to a particular show in the API
        Returns: A show object containing a complete copy of the show metadata corresponding to the media_id
        """
        data = request_to_dict("https://api.themoviedb.org/3/tv/" + str(media_id) + "?api_key=" + self.API_KEY)
        show = Show(data.get('id'), data.get('name'), data.get('overview'), data.get('first_air_date'), data.get('vote_average'), self.thumbnail_gen(data.get('poster_path')))
        if 'success' in data:
            tmp = Show(media_id, 'Invalid', 'Invalid', 'Invalid', 0, "static/cover_not_found.gif")
            tmp.cover_url = "static/cover_not_found.gif"
            return tmp
        show.runtime = 0
        if len(data.get('episode_run_time') != 0):
            show.runtime = data.get('episode_run_time')[0]
        show.language = data.get('original_language')
        show.genres = data.get('genres')
        show.cover_url = self.cover_gen(data.get('poster_path'))
        show.total_episodes = data.get('number_of_episodes')
        show.total_seasons = data.get('number_of_seasons')
        show.seasons = self.init_season_list(data);
        return show

    def init_season_list(self, data) -> list:
        """
        Creates a list containing season info for a particular show
        Parameters: data(dict): dictionary returned by a call to request_to_dict() on a valid API link to a show
        Returns: A list containing season info for a particular show
        """
        return [Season(i.get('id'), i.get('name'), i.get('overview'), i.get('episode_count'), i.get('air_date'), self.thumbnail_gen(i.get('poster_path')), self.cover_gen(i.get('poster_path'))) for i in data.get('seasons')]

    def recommend(self, media_id, MEDIA_TYPE) -> list:
        """
        Get recommendations for a particular media_id
        Parameters: media_id(int): media id corresponding to a particular show or movie in the API
                    MEDIA_TYPE(str): string containing either "Show" or "Movie" which specifies which type of media the id corresponds to
        Returns: A list of media (either all shows or all movies) that are recommended to the user based on a certain show
        """
        t = "tv/" if MEDIA_TYPE == "Show" else "movie/"
        data = request_to_dict("https://api.themoviedb.org/3/" + t + str(media_id) + "/recommendations?api_key=" + self.API_KEY)
        media_list = []
        if MEDIA_TYPE == "Movie":
            media_list = [Movie(i.get('id'), i.get('title'), i.get('overview'), i.get('release_date'), i.get('vote_average'), self.thumbnail_gen(i.get('poster_path'))) for i in data.get('results')]
        elif MEDIA_TYPE == "Show":
            media_list = [Show(i.get('id'), i.get('name'), i.get('overview'), i.get('first_air_date'), i.get('vote_average'), self.thumbnail_gen(i.get('poster_path'))) for i in data.get('results')]
        return media_list

    def search(self, title) -> list:
        """
        Searches movies and shows by title
        Parameters: title(str): title of movie user wants to search
        Returns: A list containing movies and shows returned from API
        """
        title = title.replace(" ", "+")
        movie_data = request_to_dict("https://api.themoviedb.org/3/search/movie?api_key=" + self.API_KEY + "&query=" + title)
        show_data = request_to_dict("https://api.themoviedb.org/3/search/tv?api_key=" + self.API_KEY + "&query=" + title)

        movie_list = [Movie(i.get('id'), i.get('title'), i.get('overview'), i.get('release_date'), i.get('vote_average'), self.thumbnail_gen(i.get('poster_path'))) for i in movie_data.get('results')]

        show_list = [Show(i.get('id'), i.get('name'), i.get('overview'), i.get('first_air_date'), i.get('vote_average'), self.thumbnail_gen(i.get('poster_path'))) for i in show_data.get('results')]
        if len(movie_list) == 0:
            return show_list
        if len(show_list) == 0:
            return movie_list
        # Returns list containing movies then shows, goes back and forth so both are displayed
        return [sub[item] for item in range(min(len(movie_list), len(show_list))) for sub in [movie_list, show_list]]
