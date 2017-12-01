# Abby Gervase, Roann Yanes, and Grace Milton
#!/bin/bash


printf "\ntesting /books/:book_id\n"
/afs/nd.edu/user14/csesoft/2017-fall/anaconda3/bin/python3 tests/test_books.py

printf "\ntesting /ratings/:book_id\n"
/afs/nd.edu/user14/csesoft/2017-fall/anaconda3/bin/python3 tests/test_ratings.py

printf "\ntesting /recommendations/\n"
/afs/nd.edu/user14/csesoft/2017-fall/anaconda3/bin/python3 tests/test_recommendations_index.py

printf "\ntesting /recommendations/:num\n"
/afs/nd.edu/user14/csesoft/2017-fall/anaconda3/bin/python3 tests/test_recommendations.py

printf "\ntesting /authors/\n"
/afs/nd.edu/user14/csesoft/2017-fall/anaconda3/bin/python3 tests/test_authors_index.py

printf "\ntesting /authors/:key\n"
/afs/nd.edu/user14/csesoft/2017-fall/anaconda3/bin/python3 tests/test_authors.py

printf "\ntesting /genres/\n"
/afs/nd.edu/user14/csesoft/2017-fall/anaconda3/bin/python3 tests/test_genres_index.py

printf "\ntesting /genres/:key\n"
/afs/nd.edu/user14/csesoft/2017-fall/anaconda3/bin/python3 tests/test_genres.py

printf "testing /years/\n"
/afs/nd.edu/user14/csesoft/2017-fall/anaconda3/bin/python3 tests/test_years.py

printf "testing /books/ DELETE\n"
/afs/nd.edu/user14/csesoft/2017-fall/anaconda3/bin/python3 tests/test_books_del_only.py

printf "testing /books/\n"
/afs/nd.edu/user14/csesoft/2017-fall/anaconda3/bin/python3 tests/test_books_index.py
