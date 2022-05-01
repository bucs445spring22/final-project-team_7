import contextlib
from loginDB.loginDB import loginDB
from tinydb import TinyDB, Query
import os
from flask import Flask, request


app = Flask(__name__, instance_relative_config=True)
app.secret_key = os.environ.get("FLASK_SECRET_KEY")
app.config.from_object('config.Config')

with contextlib.suppress(OSError):
    os.makedirs(app.instance_path)

@app.route('/users', methods=('get',))
def index():
    return loginDB.all()
