# Roann Yanes
# recommendations.py

import cherrypy
import re, json
from _movie_database import _movie_database

class RecommendationsController(object):
	def __init__(self, mdb=None):
		self.mdb = mdb
		self.myd = {}
			
	def GET(self, key):
		output = {"result" : "success"}
		try:	
			recommendation = self.mdb.get_highest_rated_unvoted_movie(int(key))
			output["movie_id"] = recommendation
		except Exception as ex:
			output['result'] = 'error'
			output['message'] = str(ex)
		return json.dumps(output)
	
	def DELETE(self):
		output = { "result" : "success" }
		try:
			self.mdb.ratings.clear()
		except Exception as ex:
			output['result'] = 'error'
			output['message'] = str(ex)
		return json.dumps(output)

	def PUT(self, key):
		output = { "result" : "success" }
		the_body = cherrypy.request.body.read().decode()
		try:
			the_body = json.loads(the_body)
			self.mdb.set_user_movie_rating(int(key), the_body["movie_id"], the_body["rating"])
		except Exception as ex:
			output['result'] = 'error'
			output['message'] = str(ex)
		return json.dumps(output)
