class Season:
    def __init__(self, season_id, name, overview, episode_count, air_date, thumbnail_url, cover_url):
        self.season_id = season_id
        self.name = name
        self.overview = overview
        self.episode_count = episode_count
        self.year = air_date[0:4]
        self.date = air_date[5:10]
        self.thumbnail_url = thumbnail_url
        self.cover_url = cover_url
