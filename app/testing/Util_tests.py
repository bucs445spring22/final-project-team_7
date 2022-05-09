import sys
sys.path.insert(0, '..')
from Tmdb_api import Tmdb_api
from Util import request_to_dict, library_search, build_data, build_media, check_status
import pytest
#from tinydb import TinyDB, Query
#from tinydb.operations import add
#from tinydb.operations import delete, set

def test_request_to_dict():
    api = Tmdb_api()
    assert type({}) == type(request_to_dict("https://api.themoviedb.org/3/movie/11?api_key=d7dbb644708bdabf2a395267c0890814"))

def test_library_search():
    media_list = ["test", "TEST", "best", "Star Wars"]
    assert(library_search(media_list, "test") == ["test", "TEST"])
    assert(library_search(media_list, "Star Wars") == ["Star Wars"])

def test_build_data():
    pass

def test_build_media():
    pass

def test_check_status():
    pass
