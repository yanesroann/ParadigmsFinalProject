#       Abby Gervase, Grace Milton, and Roann Yanes
#       ratings.py -- Webservice
#       November 30, 2017

import cherrypy
import re, json
from _books_database import _books_database

class RatingsController(object):
	def __init__(self, bdb=None):
		self.bdb = bdb
		self.myd = {}
			
        # Gets rating for book
	def GET(self, key):
		output = {"result" : "success"}
		try:	
			output["rating"] = self.bdb.get_rating(int(key))
			output["book_id"] = int(key)
		except Exception as ex:
			output['result'] = 'error'
			output['message'] = str(ex)
		return json.dumps(output)
