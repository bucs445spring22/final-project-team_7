from flask import *
from flask import Flask, request
from tinydb import TinyDB, Query
from pymongo import MongoClient
from app import app
import bcrypt
import requests
import json


@app.route('/signup', methods=('GET', 'POST'))
def signup():
    db = TinyDB("loginInfo.json")
    User = Query()
    error = None
    if request.method == 'POST':
        if request.form['password'] != request.form['passwordconfirm']:
            error = 'Password confirmation incorrect. Please try again.'
        else:
            username = request.form['username']
            password = request.form['password']
            headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
            data = {'username': username, 'password':password}
            response = requests.post("http://db:8000/verifySignUp", data=json.dumps(data), headers=headers)
            results = response.json()
            app.logger.debug(f'VERIFIED: {results}')
            verified = results.get('Results')
            print("v: ",verified)
            print(type(verified))
            if verified:
                return redirect(url_for('login'))
            else:
                error = 'User name already exists. Please try again.'
                return render_template('signup.html', error=error)

            # if db.search(User.username == request.form['username']):
            #     error = 'User name already exists. Please try again.'
            #     return render_template('signup.html', error=error)
            # else:
            #     salt = bcrypt.gensalt()
            #     hashed = bcrypt.hashpw(request.form['password'].encode('utf-8'), salt)
            #     new_login = {"username": request.form['username'], "hashed": hashed.decode("utf-8"), "status": "False", "movies" : ""}
            #     db.insert(new_login)
            #     return redirect(url_for('login'))

            return redirect(url_for('login'))

    return render_template('signup.html', error=error)
