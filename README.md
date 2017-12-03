# Paradigms Final Project - Book At Me Now
## Abby Gervase, Grace Milton, Roann Yanes 

First, the server must be started by running `webservice/main.py`. Then the user must go to `student04.cse.nd.edu/agervase/book_at_me_now/`.    
Once there, they will be at the menu screen. There are three dropdown menus. The first asks for the number of books that they would like recommended. The default for this is 1. The second is optional and asks for a preferred genre. The default is all genres. The third is optional and asks for a preferred year range (as old as BC, as recent as 2017). The default for this again is any year.   
Once the user is happy with their inputs, they have two options. They can press the button labelled `Rate Books` which leads them to the rating page. Here they will be given a book title, author, rating, and image. They will be asked to rate it anywhere from 1 - 5 stars. Alternatively, there are also buttons to lead them to the recommendations page or back to the home screen.   
The second button on the home screen `Get Recommendations` will lead the user straight to the page with the books recommended for them. If they choose more books than were available, all books in the given category will be shown. The idea is, however, that the more a user rates books, the better the recommendations they will receive. For each book, the title is listed, followed by each author. Each author's name is actually a button, which will lead them to an author's page.   
The author's page lists the book title for every book an author has written that is in our data set. From this page, the user can return to their recommendations or to the home screen.  
Basically, we made it so that a user may always return to the page they used to be on or the home screen.   
