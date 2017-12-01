# Abby Gervase, Grace Milton, Roann Yanes
# reset.py

import cherrypy
import re, json

class ResetController(object):
    def __init__(self, bdb=None):
        self.myd = {}
        self.bdb = bdb
        self.book_file = "../ooapi/book_files/books.csv"
        self.genre_file = "../ooapi/book_files/books_tags.csv"

    def PUT(self):
        output = { 'result' : 'success' }
        try:
            self.bdb.books = {}
            self.bdb.load_books(self.book_file)
            self.bdb.load_genres(self.genre_file)
        except Exception as ex:
            output['result'] = 'error'
            output['message'] = str(ex)
        return json.dumps(output)
	
