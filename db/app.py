import contextlib
from model.user import User
from model.db import Database
from tinydb import TinyDB, Query
import os
import json
from flask import Flask, request


app = Flask(__name__, instance_relative_config=True)
app.secret_key = os.environ.get("FLASK_SECRET_KEY")
app.config.from_object('config.Config')

with contextlib.suppress(OSError):
    os.makedirs(app.instance_path)

@app.route('/users', methods=('GET',))
def index():
    return loginDB.all()

@app.route('/verifySignUp', methods=('POST',))
def verifySignUp():
    print(f'FORM FOR SIGN UP: {request.json}')
    print("DEBUGGER: In app.py verifySignup()")
    name = request.json.get('username')
    password = request.json.get('password')
    u = User(name, password)
    return u.add_user()

@app.route('/verifyLogin', methods=('POST',))
def verify():
    print(f'FORM: {request.json}')
    print("DEBUGGER: In app.py verify()")
    name = request.json.get('username')
    password = request.json.get('password')
    u = User(name, password)
    return u.verify_login()

@app.route('/logout', methods=('POST',))
def logout():
    name = request.json.get('username')
    pw = "123"
    u = User(name, pw)
    return u.logout()


@app.route('/lookup_library', methods=('POST',))#return db
def lookup_library():
    name = request.json.get('username')
    datab = Database(name)
    return datab.lookup_library()

@app.route('/add_movie', methods=('POST',))
def add_movie():
    name = request.json.get('username')
    print("USER WE ARE ADDING TO: ",name)
    data = request.json.get('data')
    datab = Database(name)
    return datab.add_movie(data)

@app.route('/lookup_media', methods=('POST',))
def lookup_media():
    pass