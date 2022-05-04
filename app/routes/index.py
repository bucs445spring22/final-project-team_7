from flask import Flask, request
from flask import *
from app import app
from tinydb import TinyDB, Query
from tinydb.operations import set
import bcrypt
#add global variables to define current user
import requests
import json

@app.route('/', methods=('GET', 'POST'))
def login():
    db = TinyDB("loginInfo.json")
    User = Query()
    global curUser
    curUser = None
    global userDb
    userDb= None
    error = None

    if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
            data = {'username': username, 'password':password}
            response = requests.post("http://db:8000/verifyLogin", data=json.dumps(data), headers=headers)
            results = response.json()
            app.logger.debug(f'VERIFIED: {results}')
            verified = results.get('user')
            print("v: ",verified)
            print(type(verified))
            if verified:
                return redirect(url_for('homepage', user=request.form['username']))
                
            else:
              error = 'Invalid Credentials. Please try again.'


    return render_template('login.html', error=error)