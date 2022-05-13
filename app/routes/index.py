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
    #db = TinyDB("login_info.json")
    #User = Query()
    error = None

#    if request.method == 'POST':
#        if db.search(User.username == request.form['username']):
#            ret = db.get(User.username == request.form['username'])
#            status = ret.get("status")
#            hashed = str(ret.get("hashed")).encode("utf-8")
#
#            if bcrypt.checkpw(request.form['password'].encode("utf-8"), hashed):
#                db.update(set('status', 'True'), User.username == request.form['username'])
#                return redirect(url_for('homepage', user=request.form['username']))
#            else:
#                error = 'Invalid Credentials. Please try again.'
#        else:
#            error = 'Invalid Credentials. Please try again.'
#    return render_template('login.html', error=error)
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        data = {'username': username, 'password':password}
        response = requests.post("http://db:8000/verifyLogin", data=json.dumps(data), headers=headers)
        results = response.json()
        #app.logger.debug(f'VERIFIED: {results}')
        verified = results.get('user')
        #print("v: ",verified)
        #print(type(verified))
        if verified:
            session["name"] = request.form['username']
            session["counter"] = 0
            session["res"] = []
            return redirect(url_for('homepage', user=username))
        else:
            error = 'Invalid Credentials. Please try again.'
    return render_template('login.html', error=error)
