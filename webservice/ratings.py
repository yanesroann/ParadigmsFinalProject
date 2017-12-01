# Roann Yanes
# ratings.py

import cherrypy
import re, json
from _movie_database import _movie_database

class RatingsController(object):
	def __init__(self, mdb=None):
		self.mdb = mdb
		self.myd = {}
			
	def GET(self, key):
		output = {"result" : "success"}
		try:	
			output["rating"] = self.mdb.get_rating(int(key))
			output["movie_id"] = int(key)
		except Exception as ex:
			output['result'] = 'error'
			output['message'] = str(ex)
		return json.dumps(output)
