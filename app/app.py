from flask import *
app = Flask(__name__)
app.config['SECRET_KEY'] = 'woohoo'
app.config['JSON_AS_ASCII'] = False
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
