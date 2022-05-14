from MediaEntry import MediaEntry

class Movie(MediaEntry):
    MEDIA_TYPE = "Movie"
    runtime = 0
    language = ""
    genres = {}
    cover_url = ""
