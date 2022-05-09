from tinydb import TinyDB, Query, table
#from tinydb.operations import set, Delete
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

        # if db.all()[0].doc_id == 0.0:
        #     if db.all()[0].get("title") == "Example":


        for i in range(len(db.all())):
            if db.all()[i].doc_id == data.get("media_id"):
                return {"Results": False and "Already in library"}
        
        db.insert(table.Document((data), doc_id = data.get("media_id")))

        return {"Results": True and "Added to library"}
                

