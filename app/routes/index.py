from flask import *
from app import app
from tinydb import TinyDB, Query
from tinydb.operations import set
import bcrypt

@app.route('/', methods=('GET', 'POST'))
def login():
    db = TinyDB("loginInfo.json")
    User = Query()
    error = None
    if request.method == 'POST':
        if db.search(User.username == request.form['username']):
            ret = db.get(User.username == request.form['username'])
            status = ret.get("status")
            hashed = str(ret.get("hashed")).encode("utf-8")

            if bcrypt.checkpw(request.form['password'].encode("utf-8"), hashed):
                db.update(set('status', 'True'), User.username == request.form['username'])
                return redirect(url_for('homepage', user=request.form['username']))
            else:
                error = 'Invalid Credentials. Please try again.'
        else:
            error = 'Invalid Credentials. Please try again.'
    return render_template('login.html', error=error)