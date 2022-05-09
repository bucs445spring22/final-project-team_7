from tinydb import table,TinyDB, Query
import bcrypt
from tinydb.operations import set

class User:
    """
    Constructor for User Class, takes in username and password
    """
    name=""
    password=""
    def __init__(self, name, password):
        self.name = name
        self.password = password#, password #double check

    """
    Add User to Login Database, if User already exists, return False otherwise
    encrypt password and add to database return True
    """
    def add_user(self):
        db = TinyDB("loginInfo.json")
        que = Query()
        if db.search(que.username == self.name):
            return {"Results": False and self.name}
        else:
            salt = bcrypt.gensalt()
            hashed = bcrypt.hashpw(self.password.encode("utf-8"), salt)
            new_login = {"username": self.name, "hashed": hashed.decode("utf-8"), "status": "False", "movies" : ""}
            db.insert(new_login)
            format = self.name + "_DB.json"
            userDb = TinyDB(format)
            userDb.insert(table.Document({'media_id': -1,
             'title': "Example",
             'overview': "",
             'year': "2000",
             'date': "12-12",
             'rating': 0,
             'thumbnail_url': "",
             'MEDIA_TYPE': None,
             'runtime': 0,
             'language': "",
             'genres': [],
             'cover_url': ""}, doc_id=0))
            return {"Results": True and self.name}

    """
    Verifies if User login information is correct and returns True or False
    True if it exists, False otherwise
    """
    def verify_login(self) -> bool:
        db = TinyDB("loginInfo.json")
        que = Query()
        if db.search(que.username == self.name):
            ret = db.get(que.username == self.name)
            status = ret.get("status")
            hashed = str(ret.get("hashed")).encode("utf-8")
            if bcrypt.checkpw(self.password.encode("utf-8"), hashed):
                db.update(set('status', 'True'), que.username == self.name)
                format = self.name + "_DB.json"
                userDb = TinyDB(format)
                return {"user": self.name and True}
        return {"user": self.name and False}

    def logout(self) -> bool:
        db = TinyDB("loginInfo.json")
        que = Query()
        if db.search(que.username == self.name):
            ret = db.get(que.username == self.name)
            status = ret.get("status")
            db.update(set('status', 'False'), que.username == self.name)
            return {"user": self.name and True}

        return {"user": self.name and False}

    def check_status(self) -> bool:
        db = TinyDB("loginInfo.json")
        que = Query()
        print("Before db.search")
        print("self.name: " + self.name)
        if db.search(que.username == self.name):
            ret = db.get(que.username == self.name)
            status = ret.get("status")
            print("Before ifs")
            if(status == "True"):
                print("In true if")
                return {"user": True}
            else:
                print("In false if")
                return {"user": False}
        return {"user": False}
