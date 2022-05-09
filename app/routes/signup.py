from flask import *
from tinydb import TinyDB, Query
from pymongo import MongoClient
from app import app
import bcrypt

@app.route('/signup', methods=('GET', 'POST'))
def signup():
    """
    App route for signup page
    Returns: template rendering of signup webpage
    """
    db = TinyDB("login_info.json")
    User = Query()
    error = None
    if request.method == 'POST':
        if request.form['password'] != request.form['passwordconfirm']:
            error = 'Password confirmation incorrect. Please try again.'
        else:
            if db.search(User.username == request.form['username']):
                error = 'User name already exists. Please try again.'
                return render_template('signup.html', error=error)
            else:
                salt = bcrypt.gensalt()
                hashed = bcrypt.hashpw(request.form['password'].encode('utf-8'), salt)
                new_login = {"username": request.form['username'], "hashed": hashed.decode("utf-8"), "status": "False", "movies" : ""}
                db.insert(new_login)
                db_str = request.form['username'] + "USERDB.json"
                user_db = TinyDB(db_str)
                return redirect(url_for('login'))
            return redirect(url_for('login'))
    return render_template('signup.html', error=error)
