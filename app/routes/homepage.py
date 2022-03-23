from flask import *
from app import app

@app.route('/homepage', methods=('GET', 'POST'))
def homepage():
    if request.method == 'POST':
        if request.form['search']:
            return redirect(url_for('search_results', query=request.form['search']))
    return render_template('homepage.html')