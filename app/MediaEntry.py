class MediaEntry:
    MEDIA_TYPE = ""
    def __init__(self, media_id, title, overview, release_date, rating, thumbnail_url):
        self.media_id = media_id
        self.title = title
        self.overview = overview
        self.release_date = release_date
        self.rating = rating
        self.thumbnail_url = thumbnail_url
