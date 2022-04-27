import sys
sys.path.insert(0, '..')
from Tmdb_api import Tmdb_api
from Util import request_to_dict, library_search, 
import pytest

def test_request_to_dict():
    api = Tmdb_api()
    assert type({}) == type(request_to_dict("https://api.themoviedb.org/3/movie/11?api_key=d7dbb644708bdabf2a395267c0890814"))
