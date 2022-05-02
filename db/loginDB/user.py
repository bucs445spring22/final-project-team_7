from tinydb import TinyDB, Query
import bcrypt
from tinydb.operations import set

class User:
    # def __init__(self):
    #     db = TinyDB("loginInfo.json")
    
    # def user_exist(self, username):
    #     User = Query()
    #     if db.search(User.username == username):
    #         return True
    #     else:
    #         return False
    
    # def add_user(self, username, password):
    #     User = Query()

    # @classmethod
    # def all(cls):
        
    #     db = TinyDB("loginInfo.json")
    #     print(db.all())
    #     return db.all()
    def __init__(self, name="", password=""):
        self.name, self.password = password, password #double check

    # def add_user(self, name, password):
    #     db = TinyDB("loginInfo.json")
    
    def verify_user(self) -> bool:
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
