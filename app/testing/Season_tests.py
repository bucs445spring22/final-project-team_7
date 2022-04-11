import sys
sys.path.insert(0, '..')

from Season import Season
import pytest

def test_verify_constructor():
    x = Season(10, "Test", "overview", 10, "1984-01-01", "https://www.themoviedb.org/t/p/w188_and_h282_bestv2/url.jpg", "https://www.themoviedb.org/t/p/w1280/url.jpg")
    assert x.season_id == 10
    assert x.name == "Test"
    assert x.overview == "overview"
    assert x.episode_count == 10
    assert x.year == "1984"
    assert x.date == "01-01"
    assert x.thumbnail_url == "https://www.themoviedb.org/t/p/w188_and_h282_bestv2" + "/url.jpg"
    assert x.cover_url == "https://www.themoviedb.org/t/p/w1280" + "/url.jpg"
