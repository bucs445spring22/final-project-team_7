from flask import *
from app import app
<<<<<<< HEAD
#import sqlite3
from tinydb import TinyDB, Query

=======
import sqlite3
#from tinydb import TinyDB, Query
from pymongo import MongoClient
>>>>>>> 62b69876ae1e956c4c2c4248ad80879a4b0c2798
connection = sqlite3.connect("loginInfo.db")

@app.route('/signup', methods=('GET', 'POST'))
def signup():
    db = TinyDB("loginInfo.json")
    User = Query()
    error = None
    if request.method == 'POST':
        if request.form['password'] != request.form['passwordconfirm']:
            error = 'Password confirmation incorrect. Please try again.'
        else:
            cursor = connection.cursor()
            cursor.execute("INSERT INTO login VALUES (request.form['UserName'], request.form['password'])")
            if db.search(User.userName == request.form['UserName']) is None:
                new_login = {"userName": request.form['UserName'], "passWord": request.form['password']}
                db.insert(new_login)
            else:
                error = 'User name already exists. Please try again.'
            return redirect(url_for('login'))
    return render_template('signup.html', error=error)
