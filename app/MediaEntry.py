class MediaEntry:
    MEDIA_TYPE = ""
    media_id = 0
    title = ""
    overview = ""
    year = ""
    date = ""
    rating = 0
    user_rating = 0
    thumbnail_url = ""
    def __init__(self, media_id, title, overview, release_date, rating, thumbnail_url):
        self.media_id = media_id
        self.title = title
        self.overview = overview
        if type(release_date) != type(None):
            self.year = release_date[0:4]
            self.date = release_date[5:10]
        self.rating = rating
        self.thumbnail_url = thumbnail_url
