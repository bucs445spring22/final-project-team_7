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

def test_build_show():
    pass
