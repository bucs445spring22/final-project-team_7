import sys
sys.path.insert(0, '..')

from Tmdb_api import Tmdb_api
from Movie import Movie
from Show import Show
import pytest

def test_search():
    api = Tmdb_api()
    x = Movie(10, "Test", "overview", "1984-09-28", 9, "https://path/to/poster.jpg")
    y = Show(10, "Test", "overview", "1984-09-28", 9, "https://path/to/poster.jpg")
    z = api.search("star wars")
    for i in z:
        assert (type(i) == type(x)) or (type(i) == type(y))

def test_get_movie():
    api = Tmdb_api()
    x = api.get_movie(11) # Star wars
    assert x.MEDIA_TYPE == "Movie"
    assert x.runtime == 121 
    assert x.language == "en"
    assert x.genres[0].get("name") == "Adventure"
    assert x.genres[1].get("name") == "Action"
    assert x.genres[2].get("name") == "Science Fiction"
    assert x.cover_url == "https://www.themoviedb.org/t/p/w1280" + "/6FfCtAuVAW8XJjZ7eWeLibRLWTw.jpg"

def test_get_show():
    api = Tmdb_api()
    x = api.get_show(4194) # Star Wars: The Clone Wars
    assert x.MEDIA_TYPE == "Show"
    assert x.runtime == 25
    assert x.language == "en"
    assert x.genres[0].get("name") == "Action & Adventure"
    assert x.genres[1].get("name") == "Animation"
    assert x.genres[2].get("name") == "Sci-Fi & Fantasy"
    assert x.genres[0].get("id") == 10759
    assert x.genres[1].get("id") == 16
    assert x.genres[2].get("id") == 10765
    assert x.cover_url == "https://www.themoviedb.org/t/p/w1280" + "/e1nWfnnCVqxS2LeTO3dwGyAsG2V.jpg"
    assert x.total_episodes == 133
    assert x.total_seasons == 7
    # We test only season 1 here
    assert x.seasons[1].season_id == 12278
    assert x.seasons[1].name == "Season 1"
    assert x.seasons[1].overview == ""
    assert x.seasons[1].episode_count == 22
    assert x.seasons[1].year == "2008"
    assert x.seasons[1].date == "10-03"
    assert x.seasons[1].thumbnail_url == "https://www.themoviedb.org/t/p/w188_and_h282_bestv2" + "/AiP9Qfc2pmiqCeeQHVkvDcrTST6.jpg"
    assert x.seasons[1].cover_url == "https://www.themoviedb.org/t/p/w1280" + "/AiP9Qfc2pmiqCeeQHVkvDcrTST6.jpg"
        

def test_request_to_dict():
    api = Tmdb_api()
    assert type({}) == type(api.request_to_dict("https://api.themoviedb.org/3/movie/11?api_key=d7dbb644708bdabf2a395267c0890814"))

def test_thumbnail_gen():
    api = Tmdb_api()
    assert api.thumbnail_gen("/url.jpg") == "https://www.themoviedb.org/t/p/w188_and_h282_bestv2" + "/url.jpg"

def test_cover_gen():
    api = Tmdb_api()
    assert api.cover_gen("/url.jpg") == "https://www.themoviedb.org/t/p/w1280" + "/url.jpg"
