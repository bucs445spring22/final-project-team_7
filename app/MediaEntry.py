class MediaEntry:
    MEDIA_TYPE = ""
    def __init__(self, media_id, title, overview, release_date, rating, thumbnail_url):
        self.media_id = media_id
        self.title = title
        self.overview = overview
        if type(release_date) != type(None):
            self.year = release_date[0:4]
            self.date = release_date[5:10]
        else:
            self.year = ""
            self.date = ""
        self.rating = rating
        self.thumbnail_url = thumbnail_url
