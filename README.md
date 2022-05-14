# MyMDB

## CS 445 Final Project

### Spring, 2022

### Team: Team_7
Andrew Goetz, Jin Xian Li, Yong Liu

[https://github.com/bucs445spring22/final-project-team_7.git](#)


## Getting Started

MyMDB is a user hosted watchlist for movies/shows. Users can control their own watchlist with a login and signup page. Users can search for a movie or show through a search bar powered by TMDB. From there, one can and add a movie/show to your library to keep track of watched content and display relevant information about each one. You can also rate the shows and see the overall local user ratings as well as the TMDB rating. When done using the application, one can sign out and log back in later.

### Roadmap

- [x] Add movie search
- [x] Add Ratings
- [x] Add library functions (add movie, remove movie)
- [x] Add movie metadata page
- [ ] Better UI
  
## SRS

[Software Requirements Specification](https://docs.google.com/document/d/1hX_0oUR7ZxKezjC5o5HH0mNti8qfCfBhYxw3YbTXcDA/edit)

### Prerequisites

- Python 3.9
- Flask (Version 2 or more)
- Docker
- pytest
- tinydb
- requests
- bcrypt
- gunicorn
- coverage

### Installing

- Step 1: Clone the repository with **git clone https://github.com/bucs445spring22/final-project-team_7.git**
- Step 2: Go into the project directory with **cd final-project-team_7**
- Step 3: In the command line type **docker-compose up --build -d** (If there's an error be sure to have docker installed)
- Step 4: Go onto your web browser and search **localhost** in the search bar

## Built With

* [requests](https://docs.python-requests.org/en/latest/user/quickstart/#make-a-request) - request for humans
* tinydb
* bcrypt
* gunicorn
* coverage
* pytest
* Flask (Version 2 or more)

## License

GNU General Public License v3.0

## Acknowledgments

* Professor Moore

