# Sprint 0 Meeting Notes


**Attended**: Andrew Goetz, Jin Xian Li, Yong Liu

***

## Sprint Review

###  User Story:


As a client, I want an application that I can deploy on any server running Docker.

### Sprint Requirements Attempted


**The application shall minimize required dependencies**
In order to minimize dependencies, we will containerize the application with its dependencies. 
Limit the dependency to a system that supports Docker containers.
*Status: completed*

### Completed Requirements

**Docker was implemented for the application to minimize dependencies**
Docker files included:
app.Dockerfile
db.Dockerfile
Docker-compose.yml
**Flask base added with app.py file**
Hello world base program to start.

### Incomplete Requirements

None

### The summary of the entire project:

A watchlist for movies/shows. It will have the ability to rate shows, keep track of watched shows, and display relevant information about watched shows (cover art, actors, genres, etc).
***

## Sprint Planning

## Technical Flex

0/5 requirement flexes

## Technical Debt

None

### Requirements Target:

Draft and add a new class for Single Responsibility Principle

### User Stories:

As a client, I want a program that can keep track of the shows/movies that I watch.

### Planning


Implement a MediaEntry class which incorporates different media entries like movies and TV shows.

### Action Items:

We must think about what’s to be added to the class and then write the class.

### Issues and Risks:


Obstacles could include class inheritance and finding out what fields to put in the class based on the APIs we are using.

### Team Work Assignments:

Andrew Goetz: Input on class details and coding
Jin Xian Li: Input on class details and coding
Yong Liu: Input on class details and coding

