import sys
sys.path.insert(0, '..')

from Show import Show
import pytest

def test_verify_constructor():
    x = Show(10, "Test", "overview", "1984-01-01", 9, "https://www.themoviedb.org/t/p/w188_and_h282_bestv2/url.jpg")
    assert x.media_id == 10
    assert x.title == "Test"
    assert x.overview == "overview"
    assert x.year == "1984"
    assert x.date == "01-01"
    assert x.rating == 9
    assert x.thumbnail_url == "https://www.themoviedb.org/t/p/w188_and_h282_bestv2" + "/url.jpg"
