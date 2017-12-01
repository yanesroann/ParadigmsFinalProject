#!/bin/bash



printf "testing /movies/\n"
/afs/nd.edu/user14/csesoft/2017-fall/anaconda3/bin/python3 test_movies_index.py

printf "\ntesting /movies/:movie_id\n"
/afs/nd.edu/user14/csesoft/2017-fall/anaconda3/bin/python3 test_movies.py

printf "\ntesting /ratings/:movie_id\n"
/afs/nd.edu/user14/csesoft/2017-fall/anaconda3/bin/python3 test_ratings.py

printf "\ntesting /recommendations/\n"
/afs/nd.edu/user14/csesoft/2017-fall/anaconda3/bin/python3 test_recommendations_index.py

printf "\ntesting /recommendations/:user_id\n"
/afs/nd.edu/user14/csesoft/2017-fall/anaconda3/bin/python3 test_recommendations.py

printf "\ntesting /users/\n"
/afs/nd.edu/user14/csesoft/2017-fall/anaconda3/bin/python3 test_users_index.py

printf "\ntesting /users/:users_id\n"
/afs/nd.edu/user14/csesoft/2017-fall/anaconda3/bin/python3 test_users.py

