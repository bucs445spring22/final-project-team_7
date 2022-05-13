from flask import *
from app import app
import requests
from flask_session import Session

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
@app.route('/', methods=('GET', 'POST'))
def login():
    """
    App route for login page
    Returns: template rendering of login webpage
    """
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        data = {'username': username, 'password':password}
        response = requests.post("http://db:8000/verifyLogin", data=json.dumps(data), headers=headers)
        results = response.json()
        verified = results.get('user')
        if verified:
            session["name"] = request.form['username']
            session["counter"] = 0
            session["res"] = []
            session["media_id"] = 0
            return redirect(url_for('homepage', user=username))
        else:
            error = 'Invalid Credentials. Please try again.'
    return render_template('login.html', error=error)
