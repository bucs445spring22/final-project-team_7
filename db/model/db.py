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
        return data

    def add_movie(self,data) -> bool:
        db = TinyDB(self.string)
        que = Query()
        for i in range(len(db.all())):
            if db.all()[i].doc_id == data:
                pass

        return
                

