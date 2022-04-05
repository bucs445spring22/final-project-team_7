from Movie import Movie
import pytest

def test_verify_constructor():
    x = Movie(10, "Test", "overview", "1984", 9, "https://www.themoviedb.org/t/p/w188_and_h282_bestv2/url.jpg")
    assert x.media_id == 10
    assert x.title == "Test"
    assert x.overview == "overview"
    assert x.release_date == "1984"
    assert x.rating == 9
    assert x.thumbnail_url == "https://www.themoviedb.org/t/p/w188_and_h282_bestv2" + "/url.jpg"
