import json
import requests
from Movie import Movie
from Show import Show

class MediaBuilder:
    def __init__(self, username):
        """
        MediaBuilder constructor, requires username argument.
        arguments: username(str): is used to determine the current user of the library.
        Therefore, this class must be reinitialized whenever a user is changed.
        """
        self.username = username

    def build_library(self) -> list:
        """
        Get user's library from database 
        Returns: Return user's library as a list of all movies in the library
        """
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        data = {'username': self.username}
        response = requests.post("http://db:8000/lookup_library", data=json.dumps(data), headers=headers)
        results = response.json()
        media_list = []
        for t in results.items():
            cur = t[1]
            if cur.get('MEDIA_TYPE') == "Empty":
                return [Movie(-1, "Empty", "", "2000-05-13", 9, "")];
            elif cur.get('MEDIA_TYPE') == "Movie":
                media_list.append(self.build_movie(cur))
            elif cur.get('MEDIA_TYPE') == "Show":
                media_list.append(self.build_show(cur))
        return media_list

    def build_media(self, media_id):
        """
        Gets a certain MediaEntry from the user's library from the database
        Arguments: media_id(int): int corresponding to a particular movie
        Returns: Return the MediaEntry corresponding to the requested media_id, either a Show or a Movie. Returns None on error
        """
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        data = {'username': self.username, 'media_id': media_id}
        response = requests.post("http://db:8000/lookup_media", data=json.dumps(data), headers=headers)
        media = response.json()
        if media.get('MEDIA_TYPE') == "Movie":
            return self.build_movie(media)
        elif media.get('MEDIA_TYPE') == "Show":
            return self.build_show(media)
        return None

    def build_movie(self, media) -> Movie:
        """
        Builds a movie object from media dict
        arguments: media(dict): dict containing movie metadata
        return: Movie object with media_id containing metadata from media
        """
        release_date = None
        if type(media.get('year')) != type(None) and type(media.get('date')) != type(None):
            release_date = (media.get('year') + "-" + media.get('date'))
        print(media.get('media_id'))
        movie = Movie(media.get('media_id'), media.get('title'), media.get('overview'), release_date, media.get('rating'), media.get('thumbnail_url'))
        movie.user_rating = media.get('user_rating')
        movie.runtime = media.get('runtime')
        movie.language = media.get('language')
        movie.genres = media.get('genres')
        movie.cover_url = media.get('cover_url')
        return movie

    def build_show(self, media) -> Show:
        """
        Builds a show object from media dict
        arguments: media(dict): dict containing show metadata
        return: Show object containing metadata from media dict
        """
        release_date = None
        if type(media.get('year')) != None and type(media.get('date')) != None:
            release_date = (media.get('year') + "-" + media.get('date'))
        show = Show(media.get('media_id'), media.get('title'), media.get('overview'), release_date, media.get('rating'), media.get('thumbnail_url'))
        show.user_rating = media.get('user_rating')
        show.runtime = media.get('runtime')
        show.language = media.get('language')
        show.genres = media.get('genres')
        show.cover_url = media.get('cover_url')
        show.total_episodes = media.get('total_episodes')
        show.total_seasons = media.get('total_seasons')
        #show.seasons = self.init_season_list(media)
        return show
