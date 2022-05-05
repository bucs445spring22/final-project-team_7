from tinydb import TinyDB, Query
import bcrypt
from tinydb.operations import set

class Database:
    def __init__(self, username = ""):
        self.username = username
        string = username + "_DB.json"
        self.db = TinyDB(string)

    def lookup_library(self):
        que = Query()
        print(self.db.all())

        return "hi"