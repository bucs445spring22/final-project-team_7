from flask import *
from app import app
from tinydb import TinyDB, Query
from pymongo import MongoClient

@app.route('/', methods=('GET', 'POST'))
def login():
    db = TinyDB("loginInfo.json")
    User = Query()
    error = None
    if request.method == 'POST':
        if db.search(User.username == request.form['username']) and db.search(User.password == request.form['password']):
            return redirect(url_for('homepage'))
        else:
            error = 'Invalid Credentials. Please try again.'
    return render_template('login.html', error=error)