from tinydb import TinyDB, Query
from tinydb.operations import set
import json

class Database:
    def __init__(self, username = ""):
        self.username = username
        self.string = username + "_DB.json"
        self.db = TinyDB(self.string)
    
    def lookup_library(self):
        with open(self.string) as json_file:
            data = json.load(json_file)

        # print("HIHIHIHIHIHIHIHIHIHIHIHIHIHIHIHIHIHIHIHIH")
        # moviesList = {}
        # for i in self.db.all():
        #     movies[ i.get('name')] = i.get('email')
        #     #moviesList[i.get('media_id')] = i.get('movieInfo')
        return data