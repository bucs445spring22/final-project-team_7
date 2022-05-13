from tinydb import TinyDB, Query
import bcrypt
from tinydb.operations import set

class User:
    name=""
    password=""
    def __init__(self, name, password):
        """
        Constructor for User Class, takes in username and password
        """
        self.name = name
        self.password = password

    def add_user(self):
        """
        Add User to Login Database, if User already exists, return False otherwise
        encrypt password and add to database return True
        """
        db = TinyDB("loginInfo.json")
        que = Query()
        if db.search(que.username == self.name):
            return {"Results": False and self.name}
        else:
            salt = bcrypt.gensalt()
            hashed = bcrypt.hashpw(self.password.encode("utf-8"), salt)
            new_login = {"username": self.name, "hashed": hashed.decode("utf-8"), "status": "False", "movies" : ""}
            db.insert(new_login)
            return {"Results": True and self.name}

    def verify_login(self):
        """
        Verifies if User login information is correct and returns True or False
        Returns a dict with status either true or false indicating outcome
        """
        db = TinyDB("loginInfo.json")
        que = Query()
        if db.search(que.username == self.name):
            ret = db.get(que.username == self.name)
            #status = ret.get("status")
            hashed = str(ret.get("hashed")).encode("utf-8")
            if bcrypt.checkpw(self.password.encode("utf-8"), hashed):
                db.update(set('status', 'True'), que.username == self.name)
                #format = self.name + "_DB.json"
                #userDb = TinyDB(format)
                return {"user": self.name and True}
        return {"user": self.name and False}

    def logout(self):
        """
        Logs a user out, requiring user to log back in to access their library
        Returns a dict with status either true or false indicating outcome
        """
        db = TinyDB("loginInfo.json")
        que = Query()
        if db.search(que.username == self.name):
            #ret = db.get(que.username == self.name)
            #status = ret.get("status")
            db.update(set('status', 'False'), que.username == self.name)
            return {"user": self.name and True}
        return {"user": self.name and False}
