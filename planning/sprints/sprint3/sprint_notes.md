# Sprint 3 Meeting Notes

**Attended**: Andrew Goetz, Jin Xian Li, Yong Liu

***

## Sprint Review

### SRS Sections Updated

- Added 2 functional requirements
- Ability to store information in a database
- Ability to search for a movie
- Added 3 non-functional requirements
		- Scalability
		- Reliability
		- Security
- Added testing for 2 classes
		- Tmdb_api
		- Movie
 
###  User Story:

- As a user I want to be able to make an account and have my login credentials saved.
- As a confused media watcher, I want it to be easy to add new media to my library.
- As a movie watcher, I want a reliable way to search for movies.

### Requirement Implemented

- Ability to search for a movie
- Ability to fetch movie metadata from TMDB

### Completed Items

- Added ability to search for movies and display results with a well formatted UI
- Decided to use TinyDB for database to store information

### Uncompleted Items

None

### The summary of the entire project:

A watchlist for movies/shows. It will have the ability to rate shows, keep track of watched shows, and display relevant information about watched shows (cover art, actors, genres, etc).

***

## Sprint Planning

### Requirement Target:

- Ability to login and manage a user account
- Ability to store information in a database
- Scalability

### User Stories:

- I want to be able to login with a user account that I signed up with before and access the information that my account has.
- As a user I want to be able to make an account and not have to make a new one every time.
- As a confused media watcher, I want a system where if I want another type of media added, it would be easily done. 

### Planning

Fix error with TinyDB where importing doesn’t work. Add buttons for adding to the watchlist next to the movie after searching. Link back to my library after searching. Database should be able to store user signup information for login. Add show searching as another option.

### Action Items:

We must create user accounts for the development of our application to proceed.  The database must be functional and able to communicate with the main application.  The frontend must continue development.

### Issues and Risks:

Implementing user login credentials poses a serious security risk to the application if not developed properly.

### Team Work Assignments:

- Andrew will implement support for shows with a Show class and adding show results to Tmdb_api’s search function
- Andrew will further refine testing in the application and better organize class inheritance
- Yong will continue designing database, getting it to store user login information and the user’s library of media
- Ronald will continue frontend development
- Ronald and Yong will collaborate to implement user accounts into the application
