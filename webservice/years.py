# Abby Gervase, Grace Milton, Roann Yanes
# years.py

import cherrypy
import re, json
from _books_database import _books_database

class YearsController(object):
    def __init__(self, bdb=None):
        self.bdb = bdb
        self.myd = {}
			
    def GET(self, key):
        output = {"result" : "success"}
        try:
            books = self.bdb.get_books_by_year(int(key))
            output["books"] = books
            output["year"] = int(key)
        except Exception as ex:
            output['result'] = 'error'
            output['message'] = str(ex)
        return json.dumps(output)
