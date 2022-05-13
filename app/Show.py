from MediaEntry import MediaEntry

class Show(MediaEntry):
    MEDIA_TYPE = "Show"
    runtime = 0
    language = ""
    genres = {}
    cover_url = ""
    total_episodes = 0
    total_seasons = 0
    seasons = []
