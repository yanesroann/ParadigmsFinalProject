# Webservice Deliverable
## Abby Gervase, Grace Milton, Roann Yanes

This webservice interacts with the previously built OO API. The webserivce uses
port 51082.

There are 7 helper files in addition to the main.py file to create the cherrypy
server.

For `/books/`, a user can `GET` a list of the books and their authors, titles, 
years of publication, and id numbers. The user may also `POST` to add a new
book and its data. Finally, a user may `DELETE` the book database.    

To `POST` to `/books/`, the user should use the format: `{“authors”: [“Amie Kaufman”,”Jay Kristoff”], “title”: “Illuminae”, “year”: 2015}`     

A user can also access `/books/:key`, where they can `GET` a specific book and
its authors, title, year of publication, and id number. The user may also `PUT`
to update a book or add a book to a specific id number. Finally, a user may 
`DELETE` a specific book.    

To `PUT` to `/books/:key`, the user should use the format : `{“authors”: [“Amie Kaufman”,”Jay Kristoff”], “title”: “Illuminae”, “year”: 2015}`

For `/recommendations/`, a user can get a specific number of recommendations
(using `/recommendations/:num`), add a rating for a specific book with a `PUT`
command, and `DELETE` the recommendations they had given so far.    

To `PUT` to `/recommendations/`, the user should use the formatL `{“id”: 777777, “rating”: 4}`

For `/authors/` the user can `GET` a list of all the authors and the ids of
the book that have they have written or use `/authors/:key` to get a list of the
books that a specific author has written (where the `key` is the author's id 
number).

For `/genres/` the user can `GET` a list of all the genres and the ids of the
book that have been assigned that genre or use `/genres/:key` to get a list of
the books that fall under a specific genre (where the `key` is the genre's id 
number).

For `/years/:key`, the user can get a list of the books written in a certain
year (where the `key` is the desired year).

For `/ratings/:key`, the user can get the rating of the given book (where the 
`key` is the desired book id).

First, the server must be started by running `webservice/main.py`. Then the user must go to `student04.cse.nd.edu/agervase/book_at_me_now/`.
Once there, they will be at the menu screen. There are three dropdown menus. The first asks for the number of books that they would like recommended. The default for this is 1. The second is optional and asks for a preferred genre. The default is all genres. The third is optional and asks for a preferred year range (as old as BC, as recent as 2017). The default for this again is any year.
Once the user is happy with their inputs, they have two options. They can press the button labelled `Rate Books` which leads them to the rating page. Here they will be given a book title, author, rating, and image. They will be asked to rate it anywhere from 1 - 5 stars. Alternatively, there are also buttons to lead them to the recommendations page or back to the home screen.
The second button on the home screen `Get Recommendations` will lead the user straight to the page with the books recommended for them. If they choose more books than were available, all books in the given category will be shown. The idea is, however, that the more a user rates books, the better the recommendations they will receive. For each book, the title is listed, followed by each author. Each author's name is actually a button, which will lead them to an author's page.
The author's page lists the book title for every book an author has written that is in our data set. From this page, the user can return to their recommendations or to the home screen.
Basically, we made it so that a user may always return to the page they used to be on or the home screen.

ADDITIONAL NOTE: THIS PRODUCT WORKS BEST ON GOOGLE CHROME. IT DOES NOT WORK ON SAFARI.   

```
 ________   _     _   _______  
|___  ___| | |   | | |  _____| 
   | |     | |___| | | |__     
   | |     |  ___  | |  __|    
   | |     | |   | | | |_____  
   |_|     |_|   |_| |_______| 

 _______   __     _   ______ 
|  _____| |  \   | | | ___  \ 
| |__     | | \  | | | |  \  |
|  __|    | |\ \ | | | |   | |
| |_____  | | \ \| | | |__/  | 
|_______| |_|  \___| |______/ 

```
