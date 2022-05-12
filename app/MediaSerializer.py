from Movie import Movie
from Show import Show

class MediaSerializer:
    #NOTE MediaSerializer will not handle network request to db, will only get Media into a json which is then sent to db for storage

    #def __init__(self, username):
    #    """
    #    MediaSerializer constructor, requires username argument.
    #    arguments: username(str): is used to determine the current user of the library.
    #    Therefore, this class must be reinitialized whenever a user is changed.
    #    """
    #    self.username = username

    def serialize_media(self, media) -> dict:
        """
        Converts a MediaEntry to an equivalent dict, for storage in db.
        arguments: media(MediaEntry): a MediaEntry, or a type which extends MediaEntry, in which we convert to dict
        Returns: media as a dict
        """
        ret = {'media_id': media.media_id,
               'title': media.title,
               'overview': media.overview,
               'year': media.year,
               'date': media.date,
               'rating': media.rating,
               'thumbnail_url': media.thumbnail_url,
               'MEDIA_TYPE': media.MEDIA_TYPE}
        #if media.MEDIA_TYPE == "Movie" or media.MEDIA_TYPE == "Show":
        ret.update({'runtime': media.runtime,
                    'language': media.language,
                    'genres': media.genres,
                    'cover_url': media.cover_url})
        if media.MEDIA_TYPE == "Show":
            ret.update({'total_episodes': media.total_episodes,
                        'total_seasons': media.total_seasons})
        return ret
