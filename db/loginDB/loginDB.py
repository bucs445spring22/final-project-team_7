from tinydb import TinyDB, Query

class loginDB:
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
    def __init__(self, name="", email=""):
        self.name, self.email = name, email

    @classmethod
    def all(cls):
        return {
        'swag': ["thor@heimdall.com", 1500],
        'Loki': ["loki@heimdall.com", 1000],
        'Valkyrie': ["valkyrie@heimdall.com", 5000],
        }
