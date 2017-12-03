#       Abby Gervase, Grace Milton, and Roann Yanes
#       recommendations.py -- Webservice
#       November 30, 2017

import cherrypy
import re, json
from _books_database import _books_database

class RecommendationsController(object):
    def __init__(self, bdb=None):
        self.bdb = bdb
        self.myd = {}

    # Retrieves to read list for user; returns num number of books
    def GET(self, num, early, late, genre):
        output = {"result" : "success"}
        try:	
            recommendations = self.bdb.get_highest_rated_unvoted_book(int(num), int(early), int(late), int(genre))
            output["book_id"] = recommendations
        except Exception as ex:
            output['result'] = 'error'
            output['message'] = str(ex)
        return json.dumps(output)

    # Removes all ratings and recommendations
    def DELETE(self):
        output = { "result" : "success" }
        try:
            self.bdb.ratings.clear()
            self.bdb.recommendations.clear()
            self.bdb.voted_books.clear()
        except Exception as ex:
            output['result'] = 'error'
            output['message'] = str(ex)
        return json.dumps(output)

    # Sends a rating for a book
    def POST(self):
        output = { "result" : "success" }
        the_body = cherrypy.request.body.read().decode()

        try:
            the_body = json.loads(the_body)
            print(the_body)
            self.bdb.set_book_rating(the_body["id"], the_body["rating"])
            print(self.bdb.voted_books)
        except Exception as ex:
            output['result'] = 'error'
            output['message'] = str(ex)
        return json.dumps(output)
