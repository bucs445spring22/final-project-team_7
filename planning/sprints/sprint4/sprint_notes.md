# Sprint 4 Meeting Notes

**Attended**: Andrew Goetz, Jin Xian Li, Yong Liu

***

## Sprint Review

### SRS Sections Updated

Added top-level section for User Interface
 
###  User Story:

I want to be able to login with a user account that I signed up with before and access the information that my account has.
As a user I want to be able to make an account and not have to make a new one every time.
As a confused media watcher, I want a system where if I want another type of media added, it would be easily done.
As a user I want to be able to make a secure account and not have to make a new one every time.

### Sprint Requirements Attempted

Ability to login and manage a user account
Ability to store information in a database

### Completed Items

Fixed TinyDB error and added password hashing for (temporary?) TinyDB database
Added TinyDB for signup and login where it remembers users now
Further tests for application has been added
Support for shows has been added

### Incomplete Items

None

### The summary of the entire project:

A watchlist for movies/shows. It will have the ability to rate shows, keep track of watched shows, and display relevant information about watched shows (cover art, actors, genres, etc).

***

## Sprint Planning

### Requirement Target:

- Ability to add movies to the library
- Ability to manage account


### User Stories:

I want to be able to login with a user account and add movies to the library in order to append them to my list.

### Planning

Continue refining UI, adding UI elements to support user actions such as adding/removing media from library.  Want to be able to get movies into a user library now that user accounts are working.

### Action Items:

Continue development of user accounts: need a way for a particular user to access their media library and add to it.  Database should continue to be revamped.

### Issues and Risks:

Current implementation of the database uses TinyDB, we may want to switch to another solution to achieve scalability requirements.

### Team Work Assignments:

Andrew will continue backend/API development + refining tests.
Yong will adjust database to store movies.
Ronald will make necessary frontend changes to support adding/removing movies to the user library and viewing those movies on the user’s homepage.
