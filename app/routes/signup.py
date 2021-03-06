from flask import *
from app import app
import requests

@app.route('/signup', methods=('GET', 'POST'))
def signup():
    """
    App route for signup page
    Returns: template rendering of signup webpage
    """
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
            verified = results.get('Results')
            if verified:
                return redirect(url_for('login'))
            error = 'User name already exists. Please try again.'
            return render_template('signup.html', error=error)
    return render_template('signup.html', error=error)
