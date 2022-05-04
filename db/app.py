import contextlib

from loginDB.user import User
from tinydb import TinyDB, Query
import os
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
