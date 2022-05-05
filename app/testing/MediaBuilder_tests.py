import pytest
import sys
sys.path.insert(0, '..')

from MediaBuilder import MediaBuilder
from Tmdb_api import Tmdb_api

def test_build_library():
    pass

def test_build_media():
    pass

def test_build_movie():
    media = {'media_id': 11, 'title': "Star Wars", 'overview': "Princess Leia is captured and held hostage by the evil Imperial forces in their effort to take over the galactic Empire. Venturesome Luke Skywalker and dashing captain Han Solo team together with the loveable robot duo R2-D2 and C-3PO to rescue the beautiful princess and restore peace and justice in the Empire.", 'year': "1977", 'date': "05-25", 'rating': 8.2, 'thumbnail_url': "https://www.themoviedb.org/t/p/w188_and_h282_bestv2/6FfCtAuVAW8XJjZ7eWeLibRLWTw.jpg", 'runtime': 121, 'language': "en", 'genres': [ {'id': 12, 'name': "Adventure"}, {'id': 28, 'name': "Action"}, {'id': 878, 'name': "Science Fiction"} ], 'cover_url': "https://www.themoviedb.org/t/p/w1280/6FfCtAuVAW8XJjZ7eWeLibRLWTw.jpg"}
    builder = MediaBuilder("admin")
    api = Tmdb_api()
    api_movie = api.get_movie(11)
    builder_movie = builder.build_movie(media)
    assert api_movie.media_id == builder_movie.media_id
    assert api_movie.title == builder_movie.title
    assert api_movie.overview == builder_movie.overview
    assert api_movie.date == builder_movie.date
    assert api_movie.MEDIA_TYPE == builder_movie.MEDIA_TYPE
    assert api_movie.rating == builder_movie.rating
    assert api_movie.thumbnail_url == builder_movie.thumbnail_url
    assert api_movie.language == builder_movie.language
    assert api_movie.runtime == builder_movie.runtime
    assert api_movie.genres == builder_movie.genres
    assert api_movie.cover_url == builder_movie.cover_url

def test_build_show():
    media = {'media_id': 4194, 'title': "Star Wars: The Clone Wars", 'overview': "Yoda, Obi-Wan Kenobi, Anakin Skywalker, Mace Windu and other Jedi Knights lead the Grand Army of the Republic against the droid army of the Separatists.", 'year': "2008", 'date': "10-03", 'rating': 8.5, 'thumbnail_url': "https://www.themoviedb.org/t/p/w188_and_h282_bestv2/e1nWfnnCVqxS2LeTO3dwGyAsG2V.jpg", 'runtime': 25, 'language': "en", 'genres': [ {'id': 10759, 'name': "Action & Adventure"}, {'id': 16, 'name': "Animation"}, {'id': 10765, 'name': "Sci-Fi & Fantasy"} ], 'cover_url': "https://www.themoviedb.org/t/p/w1280/e1nWfnnCVqxS2LeTO3dwGyAsG2V.jpg", 'total_episodes': 133, 'total_seasons': 7}
    builder = MediaBuilder("admin")
    api = Tmdb_api()
    api_show = api.get_show(4194)
    builder_show = builder.build_show(media)
    assert api_show.media_id == builder_show.media_id
    assert api_show.title == builder_show.title
    assert api_show.overview == builder_show.overview
    assert api_show.date == builder_show.date
    assert api_show.MEDIA_TYPE == builder_show.MEDIA_TYPE
    assert api_show.rating == builder_show.rating
    assert api_show.thumbnail_url == builder_show.thumbnail_url
    assert api_show.language == builder_show.language
    assert api_show.runtime == builder_show.runtime
    assert api_show.genres == builder_show.genres
    assert api_show.cover_url == builder_show.cover_url
    assert api_show.total_episodes == builder_show.total_episodes
    assert api_show.total_seasons == builder_show.total_seasons
