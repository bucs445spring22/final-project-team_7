# Sprint 5 Meeting Notes

**Attended**: Andrew Goetz, Jin Xian Li, Yong Liu

***

## Sprint Review

### SRS Sections Updated

Added top-level section for coverage output

Adjusted many non-functional requirements
 
###  User Story:
 
I want to be able to login with a user account that I signed up with before and access the information that my account has.

As a confused media watcher, I want a system where if I want another type of media added, it can be easily done.

### Sprint Requirements Attempted

Ability to add movies to the library

Ability to manage account

### Completed Items

Media is now displayed in the user’s library and can be added to the library.

Additional testing has been added for shows/seasons, and coverage screenshot was added to SRS along with a revamp of non-functional requirements.

### Incomplete Items

None

### The summary of the entire project:

A watchlist for movies/shows. It will have the ability to rate shows, keep track of watched shows, and display relevant information about watched shows (cover art, actors, genres, etc).

***

## Sprint Planning

### Requirement Target:

Ability to give a rating to a movie

Ability to see metadata about a searched movie

Ability to remove a movie

### User Stories:

After I finish watching a movie or TV Show, I would like to be able to rate it from 1-10 stars. I would leave a 1 star rating if I disliked the movie/show or a 10 star rating if I enjoyed it.

I want to be able to look at the movies and their information that I add to my list

As a user I want to be able to remove a media from my library.

### Planning

Should get started on rating system: the rating system should average all ratings together into a global rating for the MediaEntry. This global rating may require storage in the database that is not associated with any particular account (since all should be able to access it).

Other major thing that has to get done is a webpage to display more detailed information about a MediaEntry, accessible by clicking on a MediaEntry in search results or in library.

### Action Items:

Complete rating system, display more in depth information about MediaEntry in dedicated page. Increases testing. Implement removal of media.

### Issues and Risks:

Want to ensure database is scaling properly with increased feature load (ratings).

Want to ensure we aren’t making unnecessary network requests, better to store stuff like images locally as well if possible.

### Team Work Assignments:

Yong do database stuff.

Andrew do backend to support ratings + testing + paperwork.

Jin Xian Li do frontend stuff to support aforementioned features and removing movie from db.

Everyone determine how to better test their part of the application and write those tests.
