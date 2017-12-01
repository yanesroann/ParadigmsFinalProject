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
