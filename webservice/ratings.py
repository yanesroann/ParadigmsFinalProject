# Roann Yanes
# ratings.py

import cherrypy
import re, json
from _books_database import _books_database

class RatingsController(object):
	def __init__(self, bdb=None):
		self.bdb = bdb
		self.myd = {}
			
	def GET(self, key):
		output = {"result" : "success"}
		try:	
			output["rating"] = self.bdb.get_rating(int(key))
			output["book_id"] = int(key)
		except Exception as ex:
			output['result'] = 'error'
			output['message'] = str(ex)
		return json.dumps(output)
