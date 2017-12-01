# Roann Yanes
# reset.py

import cherrypy
import re, json

class ResetController(object):
	def __init__(self, mdb=None):
		self.myd = {}
		self.mdb = mdb
		self.movie_file = "/home/paradigms/ml-1m/movies.dat"
		self.image_file = "/home/paradigms/images.dat"
		self.rating_file = "/home/paradigms/ml-1m/ratings.dat"
		self.user_file = "/home/paradigms/ml-1m/users.dat"

	def PUT(self):
		output = { 'result' : 'success' }
		try:
			self.mdb.load_movies(self.movie_file)
			self.mdb.load_users(self.user_file)
			self.mdb.load_ratings(self.rating_file)
			self.mdb.load_images(self.image_file)
		except Exception as ex:
			output['result'] = 'error'
			output['message'] = str(ex)
		return json.dumps(output)
	
	def PUT_KEY(self, key):
		output = { 'result' : 'success' }
		try:
			for line in open(self.movie_file, "r"):
				fields = line.strip().split("::")
				if int(fields[0]) == int(key):
					self.mdb.set_movie(int(key), fields[1:])
			for line in open(self.user_file, "r"):
				fields = line.strip().split("::")
				if int(fields[0]) == int(key):
					self.mdb.set_user(int(key), [fields[1], int(fields[2]), int(fields[3]), fields[4]])
				
			for line in open(self.rating_file, "r"):
				fields = line.strip().split("::")
				if int(fields[0]) == int(key):
					if int(fields[1]) not in self.mdb.ratings:
						self.mdb.ratings[int(fields[1])] = {}
						self.ratings[int(fields[1])].update({int(fields[0]): float(fields[2])})
			for line in open(self.image_file, "r"):
				fields = line.strip().split("::")
				if int(fields[0]) == int(key):
					self.mdb.set_image(int(key), fields[2])
		except Exception as ex:
			output['result'] = 'error'
			output['message'] = str(ex)
		return json.dumps(output)
