# `_books_database.py` -- OO API
## Abby Gervase, Grace Milton, Roann Yanes

Our OO API is an expanded version of the movie database. We are using book data 
to load in the info for ratings, title, year, book id, authors, and images of 
various books. From another file we read in genre info for each book. Our goal
was to able to access or narrow down books by many different field to better
customize user experience. We have the basic methods to get and set books by ID
but we can also get books by year, genre, or author. At the end, we hope to
allow the user to narrow down by field the books they want. Once they do this,
we will present them with a list of books for them to rate if they have read
them. Once these books have been rated, we will generate a to-read list for
them of a length of their choosing. We had to create a formula to compute the
ratings based on how the ratings were stored in the data. We also devised a way
to get the highest rated unvoted book(s).
