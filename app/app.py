from flask import *
app = Flask(__name__)

@app.route('/')
def render():
    print("Hello world")

def main():
    app.run()
    team = {
         "Team Member 1": "Andrew Goetz", 
         "Team Member 2": "Jin Xian Li",
         "Team Member 3": "Yong Liu",
    }

if __name__ == "__main__":
    main()
