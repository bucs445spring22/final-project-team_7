import pytest
import sys
sys.path.insert(0, '..')

from HtmlBuilder import HtmlBuilder
from Tmdb_api import Tmdb_api

def test_build_homepage():
    api = Tmdb_api()
    library = [ api.get_movie(11), api.get_show(4194) ]
    builder = HtmlBuilder()
    assert type(builder.build_homepage(library, "admin")) == str

def test_build_mediaview():
    api = Tmdb_api()
    movie = api.get_movie(11)
    builder = HtmlBuilder()
    assert type(builder.build_mediaview(movie)) == str
