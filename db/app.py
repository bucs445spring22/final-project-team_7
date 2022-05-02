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


@app.route('/verify', methods=('POST',))
def verify():
    print(f'FORM: {request.json}')
    # name = request.form['username']
    # password = request.form['password'].encode("utf-8")
    # u = User(name, password)
    print("In app.py print")
    name = request.json.get('username')
    password = request.json.get('password')
    u = User(name, password)
    return u.verify_user()
