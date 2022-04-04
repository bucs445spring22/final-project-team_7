from Tmdb_api import Tmdb_api
from Movie import Movie
import pytest

def test_search():
    api = Tmdb_api();
    x = Movie(10, "Test", "overview", "1984", 9, "/url.jpg")
    assert type(api.search("star wars")[1]) == type(x)


def test_get_movie():
    api = Tmdb_api();
    x = api.get_movie(11); # Star wars
    assert x.runtime == 121 
    assert x.language == "en"
    assert x.genres[0].get("name") == "Adventure"
    assert x.genres[1].get("name") == "Action"
    assert x.genres[2].get("name") == "Science Fiction"
    assert x.cover_url == "https://www.themoviedb.org/t/p/w1280" + "/6FfCtAuVAW8XJjZ7eWeLibRLWTw.jpg"
