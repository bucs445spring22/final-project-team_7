from flask import Flask, render_template, request


import contextlib
import os

app = Flask(__name__)
app.config.from_pyfile('config.py')
app.secret_key = os.environ.get("SECRET_KEY")

# ensure the instance folder exists
with contextlib.suppress(OSError):
    os.makedirs(app.instance_path)


import routes.index
import routes.signup
import routes.homepage
import routes.search_results

def main():
    app.run()
    team = {
         "Team Member 1": "Andrew Goetz", 
         "Team Member 2": "Jin Xian Li",
         "Team Member 3": "Yong Liu",
    }

if __name__ == "__main__":
    main()
