from flask import *
app = Flask(__name__)
app.config['SECRET_KEY'] = 'woohoo'

@app.route('/', methods=('GET', 'POST'))
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('homepage'))
    return render_template('login.html', error=error)

@app.route('/signup', methods=('GET', 'POST'))
def signup():
    return "Hello world"

@app.route('/homepage', methods=('GET', 'POST'))
def homepage():
    return render_template('homepage.html')


def main():
    app.run()
    team = {
         "Team Member 1": "Andrew Goetz", 
         "Team Member 2": "Jin Xian Li",
         "Team Member 3": "Yong Liu",
    }

if __name__ == "__main__":
    main()
