import pytest
import sys
sys.path.insert(0, '../../db/')

from model.db import Database

#NOTE at end of each test, we drop TEST_USER table to ensure tests remain correct

show = {'media_id': 4194,
        'title': "Star Wars: The Clone Wars",
        'overview': "Yoda, Obi-Wan Kenobi, Anakin Skywalker, Mace Windu and other Jedi Knights lead the Grand Army of the Republic against the droid army of the Separatists.",
        'year': "2008",
        'date': "10-03",
        'rating': 8.5,
        'thumbnail_url': "https://www.themoviedb.org/t/p/w188_and_h282_bestv2/e1nWfnnCVqxS2LeTO3dwGyAsG2V.jpg",
        'runtime': 25,
        'language': "en",
        'genres': [{'id': 10759, 'name': "Action & Adventure"},
                   {'id': 16, 'name': "Animation"},
                   {'id': 10765, 'name': "Sci-Fi & Fantasy"}],
        'cover_url': "https://www.themoviedb.org/t/p/w1280/e1nWfnnCVqxS2LeTO3dwGyAsG2V.jpg",
        'total_episodes': 133,
        'total_seasons': 7}

movie = {'media_id': 11,
         'title': "Star Wars",
         'overview': "Princess Leia is captured and held hostage by the evil Imperial forces in their effort to take over the galactic Empire. Venturesome Luke Skywalker and dashing captain Han Solo team together with the loveable robot duo R2-D2 and C-3PO to rescue the beautiful princess and restore peace and justice in the Empire.",
         'year': "1977",
         'date': "05-25",
         'rating': 8.2,
         'thumbnail_url': "https://www.themoviedb.org/t/p/w188_and_h282_bestv2/6FfCtAuVAW8XJjZ7eWeLibRLWTw.jpg",
         'MEDIA_TYPE': "Movie",
         'runtime': 121,
         'language': "en",
         'genres': [{'id': 12,'name': "Adventure"},
                    {'id': 28, 'name': "Action"},
                    {'id': 878, 'name': "Science Fiction"}],
         'cover_url': "https://www.themoviedb.org/t/p/w1280/6FfCtAuVAW8XJjZ7eWeLibRLWTw.jpg"}

def test_verify_constructor():
    db = Database("TEST_USER")
    assert db.username == "TEST_USER"
    db.db.drop_table("TEST_USER")

def test_lookup_library():
    db = Database("TEST_USER")
    print(db.lookup_library())
    assert db.lookup_library() == {'-1': {'MEDIA_TYPE': 'Empty'}}
    global movie
    db.add_media(movie)
    assert db.lookup_library() == {11: {'media_id': 11, 'title': 'Star Wars', 'overview': 'Princess Leia is captured and held hostage by the evil Imperial forces in their effort to take over the galactic Empire. Venturesome Luke Skywalker and dashing captain Han Solo team together with the loveable robot duo R2-D2 and C-3PO to rescue the beautiful princess and restore peace and justice in the Empire.', 'year': '1977', 'date': '05-25', 'rating': 8.2, 'thumbnail_url': 'https://www.themoviedb.org/t/p/w188_and_h282_bestv2/6FfCtAuVAW8XJjZ7eWeLibRLWTw.jpg', 'MEDIA_TYPE': 'Movie', 'runtime': 121, 'language': 'en', 'genres': [{'id': 12, 'name': 'Adventure'}, {'id': 28, 'name': 'Action'}, {'id': 878, 'name': 'Science Fiction'}], 'cover_url': 'https://www.themoviedb.org/t/p/w1280/6FfCtAuVAW8XJjZ7eWeLibRLWTw.jpg'}}
    db.db.drop_table("TEST_USER")

def test_lookup_media():
    db = Database("TEST_USER")
    global show
    db.add_media(show)
    assert db.lookup_media(4194) == {'media_id': 4194, 'title': 'Star Wars: The Clone Wars', 'overview': 'Yoda, Obi-Wan Kenobi, Anakin Skywalker, Mace Windu and other Jedi Knights lead the Grand Army of the Republic against the droid army of the Separatists.', 'year': '2008', 'date': '10-03', 'rating': 8.5, 'thumbnail_url': 'https://www.themoviedb.org/t/p/w188_and_h282_bestv2/e1nWfnnCVqxS2LeTO3dwGyAsG2V.jpg', 'runtime': 25, 'language': 'en', 'genres': [{'id': 10759, 'name': 'Action & Adventure'}, {'id': 16, 'name': 'Animation'}, {'id': 10765, 'name': 'Sci-Fi & Fantasy'}], 'cover_url': 'https://www.themoviedb.org/t/p/w1280/e1nWfnnCVqxS2LeTO3dwGyAsG2V.jpg', 'total_episodes': 133, 'total_seasons': 7}
    db.db.drop_table("TEST_USER")

def test_add_media():
    db = Database("TEST_USER")
    global show
    db.add_media(show)
    assert db.lookup_media(4194) == {'media_id': 4194, 'title': 'Star Wars: The Clone Wars', 'overview': 'Yoda, Obi-Wan Kenobi, Anakin Skywalker, Mace Windu and other Jedi Knights lead the Grand Army of the Republic against the droid army of the Separatists.', 'year': '2008', 'date': '10-03', 'rating': 8.5, 'thumbnail_url': 'https://www.themoviedb.org/t/p/w188_and_h282_bestv2/e1nWfnnCVqxS2LeTO3dwGyAsG2V.jpg', 'runtime': 25, 'language': 'en', 'genres': [{'id': 10759, 'name': 'Action & Adventure'}, {'id': 16, 'name': 'Animation'}, {'id': 10765, 'name': 'Sci-Fi & Fantasy'}], 'cover_url': 'https://www.themoviedb.org/t/p/w1280/e1nWfnnCVqxS2LeTO3dwGyAsG2V.jpg', 'total_episodes': 133, 'total_seasons': 7}
    db.db.drop_table("TEST_USER")

def test_remove_media():
    db = Database("TEST_USER")
    global movie
    db.add_media(movie)
    db.add_media(show)
    db.remove_media(4194)
    assert db.lookup_library() == {11: {'media_id': 11, 'title': 'Star Wars', 'overview': 'Princess Leia is captured and held hostage by the evil Imperial forces in their effort to take over the galactic Empire. Venturesome Luke Skywalker and dashing captain Han Solo team together with the loveable robot duo R2-D2 and C-3PO to rescue the beautiful princess and restore peace and justice in the Empire.', 'year': '1977', 'date': '05-25', 'rating': 8.2, 'thumbnail_url': 'https://www.themoviedb.org/t/p/w188_and_h282_bestv2/6FfCtAuVAW8XJjZ7eWeLibRLWTw.jpg', 'MEDIA_TYPE': 'Movie', 'runtime': 121, 'language': 'en', 'genres': [{'id': 12, 'name': 'Adventure'}, {'id': 28, 'name': 'Action'}, {'id': 878, 'name': 'Science Fiction'}], 'cover_url': 'https://www.themoviedb.org/t/p/w1280/6FfCtAuVAW8XJjZ7eWeLibRLWTw.jpg'}}
    db.db.drop_table("TEST_USER")
