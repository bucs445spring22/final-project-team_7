import pytest
import sys
sys.path.insert(0, '..')

from HtmlBuilder import HtmlBuilder
from Tmdb_api import Tmdb_api

def test_build_homepage():
    api = Tmdb_api()
    library = [api.get_movie(11), api.get_show(4194)]
    builder = HtmlBuilder()
    assert builder.build_homepage(library, "admin") == "<h1 style=color:white>Welcome to your library, admin!</h1><table border=1><form method='post' action='/goto_movie_page'><td><a class='button1' value=\">Star Wars\"><button type='submit' name='mov' value='11'><img src ='https://www.themoviedb.org/t/p/w188_and_h282_bestv2/6FfCtAuVAW8XJjZ7eWeLibRLWTw.jpg'></button></a></td></form><td style=color:white width='100'>Star Wars</td><form method='post' action='/goto_movie_page'><td><a class='button1' value=\">Star Wars: The Clone Wars\"><button type='submit' name='mov' value='4194'><img src ='https://www.themoviedb.org/t/p/w188_and_h282_bestv2/e1nWfnnCVqxS2LeTO3dwGyAsG2V.jpg'></button></a></td></form><td style=color:white width='100'>Star Wars: The Clone Wars</td></table>"

def test_build_mediaview():
    api = Tmdb_api()
    movie = api.get_movie(11)
    builder = HtmlBuilder()
    assert type(builder.build_mediaview(movie)) == str
