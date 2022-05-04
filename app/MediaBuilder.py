import json
import requests

class LibraryBuilder:
    def __init__(self, User):
        """
        LibraryBuilder constructor, requires User argument.
        arguments: User is used to determine the current user of the library.
        Therefore, this class must be reinitialized whenever a user is changed.
        """
        self.username = User.username

    def build_library(self) -> list:
        """
        Get user's library from database 
        Returns: Return user's library as a list of all movies in the library
        TODO: consider sorting library by title before returning
        """
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        data = {'username': self.username}
        response = requests.post("http://db:8000/lookup_library", data=json.dumps(data), headers)
        results = response.json()

        for i in results:
            

    def build_media(self, media_id);
        """
        Gets a certain MediaEntry from the user's library from the database
        Arguments: media_id(int): int corresponding to a particular movie
        Returns: Return the MediaEntry corresponding to the requested media_id
        """
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        data = {'username': self.username, 'media_id': media_id}
        response = requests.post("http://db:8000/lookup_media", data=json.dumps(data), headers)
        media = response.json()
        if MEDIA_TYPE == "Movie"
            return build_movie(media, media_id)
        elif MEDIA_TYPE == "Show"
            return build_show(media, media_id)
        return None

    def build_movie(media, media_id) -> Movie:
        pass

    def build_show(media, media_id) -> Show:
        pass
