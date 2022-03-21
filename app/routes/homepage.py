from flask import *
from app import app

@app.route('/homepage', methods=('GET', 'POST'))
def homepage():
    return render_template('homepage.html')