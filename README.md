# ParadigmsFinalProject

1. `__init__(self)` -- This method is the class constructor. It should create three data
members: self.movies is an empty dictionary (which will use the movie ID as the key),
self.users is an empty dictionary (which will use the user ID as the key), and
self.ratings, which is an empty dictionary that will use the movie ID as its key.
2. `load_movies(movie_file)` -- This method will open the file with the name given as
a parameter and load the movie data from that file into a dictionary or list of
dictionaries. The dictionary or list must be a data member of this class instance. The
load movies function should replace any existing contents of the movie data member
with the data read from the file.
3. `get_book(bid)` -- Given a book ID (an integer), returns a list with two elements or
None. If no book with the specified ID is present in the object's movie data member,
this method returns None. If the movie is present, the method returns a list of two
strings. The first string is the movie , and the second string is the movie genre.
4. `get_movies()` -- Returns a list of integers containing all movie IDs. Note: the list
should contain integers (e.g., 123), not strings (e.g., '123').
5. `set_movie(mid, [title, genres])` -- Updates the movie data member entry with
the specified movie ID, or creates a new entry if data for the movie th that ID is not
present. The title of the updated or new movie, and the list of its genres, are supplied
as parameters.
6. `delete_movie(mid)` -- This method will cause the entry with the specified movie ID
to be removed from the object's movie data member. If no such entry exists, the
movie data member is not modified.
7. `load_users(users file)` -- This method will open the file with the name given as a
parameter and load the user data from that file into a dictionary or list of dictionaries.
The dictionary or list must be a data member of this class instance. The load users
function should replace any existing contents of the user data member with the data
read from the file.
8. `get_user(uid)` -- Given an ID of a user (an integer), returns a list containing that
user's gender, age, occupation code, and zip code, in that order. The age and
occupation code should be integers, all other components are strings. If there is no
entry corresponding to that ID, None should be returned.
9. `get_users()` -- Returns a list of integers containing all user IDs.
10. `set_user(uid, [gender, age, occupationcode, zipcode])` -- Update or
create a new entry in the object's user data member. The updated or new user item's
data should be taken from the list supplied as the second parameter to the function.
The layout and format of this list matches the list returned by the get user function.
11. `delete_user(uid)` -- Removes the user with the specified user ID from the object's
user data member. If the user with that uid is not present, the user data member must
not be modified.

12. `load_ratings(ratings_file)` -- This method will open the file with the name
given as a parameter and load the ratings data from that file into a dictionary of
dictionaries, which must be a data member of the class instance. The key for this
dictionary must be a movie id, and the value is a dictionary containing ratings for the
movie with that id. The key of that dictionary is a user id, and the value is a rating
supplied by that user for that movie. You may ignore the timestamp column in the
data file. The uid, mid, and rating are all integers. Any prior contents of the rating
data member must be removed before the file is read.
13. `get_rating(mid)` -- computes and returns the average rating for a movie. The
returned average must be a float, since the average of a set of integers might not be an
integer. If there is no movie with the specified id, this method should return zero.
14. `get_highest_rated_movie()` -- Returns the ID of the movie with the highest
average rating. If more than one movie has the highest average rating, the movie with
the lowest ID wins. If there is no movie data in the object, this method returns None.
15. `set_user_movie_rating(uid, mid, rating)` -- Given a user ID, a movie ID, and
a rating, set that movie's rating from that user to that rating. If there is no user with
the given ID or no movie with the given ID, the rating data member should not be
modified.
16. `get_user_movie_rating(uid, mid)` -- Returns the specified user's rating for the
specified movie. If that user has not rated that movie, or no movie with that ID exists,
this method must return None.
17. `delete_all_ratings()` -- Clear the database of all user ratings for all movies
