from Tmdb_api import Tmdb_api
from Movie import Movie
import pytest

def test_search():
    api = Tmdb_api()
    x = Movie(10, "Test", "overview", "1984-09-28", 9, "/url.jpg")
    assert type(api.search("star wars")[1]) == type(x)

def test_get_movie():
    api = Tmdb_api()
    x = api.get_movie(11); # Star wars
    assert x.runtime == 121 
    assert x.language == "en"
    assert x.genres[0].get("name") == "Adventure"
    assert x.genres[1].get("name") == "Action"
    assert x.genres[2].get("name") == "Science Fiction"
    assert x.cover_url == "https://www.themoviedb.org/t/p/w1280" + "/6FfCtAuVAW8XJjZ7eWeLibRLWTw.jpg"

def test_request_to_dict():
    api = Tmdb_api()
    assert type({}) == type(api.request_to_dict("https://api.themoviedb.org/3/movie/11?api_key=d7dbb644708bdabf2a395267c0890814"))

def test_thumbnail_gen():
    api = Tmdb_api()
    assert api.thumbnail_gen("/url.jpg") == "https://www.themoviedb.org/t/p/w188_and_h282_bestv2" + "/url.jpg"

def test_cover_gen():
    api = Tmdb_api()
    assert api.cover_gen("/url.jpg") == "https://www.themoviedb.org/t/p/w1280" + "/url.jpg"
    
def test_date_gen():
    api = Tmdb_api()
    assert api.date_gen("1212-12-12") == "1212"
