# from MediaEntry import MediaEntry

class Movie:
    def __init__(self, genres, media_id, title, overview, poster_url, release_date, rating):
        self.genres = genres
        self.media_id = media_id
        self.title = title
        self.overview = overview
        self.poster_url = poster_url
        self.release_date = release_date
        self.rating = rating
