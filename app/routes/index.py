from flask import *
from app import app
from tinydb import TinyDB, Query
from pymongo import MongoClient
import bcrypt

@app.route('/', methods=('GET', 'POST'))
def login():
    db = TinyDB("loginInfo.json")
    User = Query()
    error = None
    if request.method == 'POST':

        if db.search(User.username == request.form['username']):
            hashed = db.get(User.username == request.form['username'])
            hashed = str(hashed.get("hashed")).encode("utf-8")
            if bcrypt.checkpw(request.form['password'].encode("utf-8"), hashed):
                return redirect(url_for('homepage'))
            else:
                error = 'Invalid Credentials. Please try again.'
        else:
            error = 'Invalid Credentials. Please try again.'
    return render_template('login.html', error=error)