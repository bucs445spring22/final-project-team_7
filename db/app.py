import contextlib
from model.user import User
from model.db import Database
#from tinydb import TinyDB, Query
import os
#import json
from flask import Flask, request

app = Flask(__name__, instance_relative_config=True)
app.secret_key = os.environ.get("FLASK_SECRET_KEY")
app.config.from_object('config.Config')

with contextlib.suppress(OSError):
    os.makedirs(app.instance_path)

@app.route('/users', methods=('GET',))
def index():
    return loginDB.all()

@app.route('/checkStatus', methods=('POST',))
def checkStatus():
    username = request.json.get('username')
    pw = "123"
    u = User(username, pw)
    return u.check_status()

@app.route('/verifySignUp', methods=('POST',))
def verifySignUp():
    #print(f'FORM FOR SIGN UP: {request.json}')
    #print("DEBUGGER: In app.py verifySignup()")
    name = request.json.get('username')
    password = request.json.get('password')
    u = User(name, password)
    return u.add_user()

@app.route('/logout', methods=('POST',))
def logout():
    name = request.json.get('username')
    pw = "123"
    u = User(name, pw)
    return u.logout()

@app.route('/lookup_library', methods=('POST',))#return db
def lookup_library():
    name = request.json.get('username')
    db = Database(name)
    return db.lookup_library()

@app.route('/lookup_media', methods=('POST',))
def lookup_media():
    username = request.json.get('username')
    media_id = request.json.get('media_id')
    #print("DEBUG:", media_id)
    db = Database(username)
    return db.lookup_media(media_id)

@app.route('/add_media', methods=('POST',))
def add_media():
    username = request.json.get('username')
    #print("USER WE ARE ADDING TO: ",username)
    data = request.json.get('data')
    #print("DATA WE ARE ADDING: ",data)
    db = Database(username)
    return db.add_media(data)

@app.route('/remove_media', methods=('POST',))
def remove_media():
    username = request.json.get('username')
    media_id = request.json.get('media_id')
    #print("DEBUG:", media_id)
    db = Database(username)
    return db.remove_media(media_id)

@app.route('/verifyLogin', methods=('POST',))
def verify():
    #print(f'FORM: {request.json}')
    #print("DEBUGGER: In app.py verify()")
    name = request.json.get('username')
    password = request.json.get('password')
    u = User(name, password)
    return u.verify_login()

@app.route('/rate', methods=('POST',))
def rate():
    media_id = request.json.get('media_id')
    rating = request.json.get('rating')
    username = request.json.get('username')
    db = Database(username)
    media = db.lookup_media(media_id)
    #print(media)
    media['user_rating'] = rating
    #print()
    #print(media)
    return db.add_media(media)
