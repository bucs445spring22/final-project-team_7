from flask import *
from app import app

@app.route('/signup', methods=('GET', 'POST'))
def signup():
    error = None
    if request.method == 'POST':
        if request.form['password'] != request.form['passwordconfirm']:
            error = 'Password confirmation incorrect. Please try again.'
        else:
            return redirect(url_for('login'))
    return render_template('signup.html', error=error)