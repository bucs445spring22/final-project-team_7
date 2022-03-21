from flask import *
from app import app

@app.route('/', methods=('GET', 'POST'))
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('homepage'))
    return render_template('login.html', error=error)