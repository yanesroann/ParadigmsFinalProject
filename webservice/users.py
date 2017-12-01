# Roann Yanes
# users.py

import cherrypy
import re, json
from _movie_database import _movie_database

class UsersController(object):
	def __init__(self, mdb=None):
		self.mdb = mdb
		self.myd = {}
		self.myd['users'] = []
		for uid in mdb.users:
			entry = { "result" : "success" }
			entry["gender"] = mdb.users[uid][0]
			entry["age"] = mdb.users[uid][1]
			entry["zipcode"] = mdb.users[uid][3]
			entry["id"] = uid
			entry["occupation"] = mdb.users[uid][2]
			self.myd["users"].append(entry)
			
	def GET(self):
		output = {}
		try:
			output = self.myd
			self.myd['users'] = []
			for uid in self.mdb.users:
				entry = { "result" : "success" }
				entry["gender"] = self.mdb.users[uid][0]
				entry["age"] = self.mdb.users[uid][1]
				entry["zipcode"] = self.mdb.users[uid][3]
				entry["id"] = uid
				entry["occupation"] = self.mdb.users[uid][2]
				self.myd["users"].append(entry)
			output["result"] = "success"
		except Exception as ex:
			output['result'] = 'error'
			output['message'] = str(ex)
		return json.dumps(output)
	
	def POST(self):
		output = { "result" : "success" }
		the_body = cherrypy.request.body.read().decode()
		try:
			the_body = json.loads(the_body)
			user = [the_body["gender"], the_body["age"], the_body["occupation"], the_body["zipcode"]]
			found = False
			for uid in self.mdb.users:
				if user == self.mdb.users[uid]:
					found = True
			if not found:
				uid = len(self.mdb.users) + 1
				while uid in self.mdb.users:
					uid += 1
				self.mdb.set_user(uid, user)
				entry = {"gender": the_body["gender"], "age": the_body["age"], "zipcode": the_body["zipcode"], "result": "success", "id": uid, "occupation": the_body["occupation"]}
				self.myd["users"].append(entry)
				output["id"] = uid
		except Exception as ex:
			output['result'] = 'error'
			output['message'] = str(ex)
		return json.dumps(output)

	def DELETE(self):
		output = { "result" : "success" }
		try:
			self.mdb.users.clear()
			self.mdb.images.clear()
			self.mdb.ratings.clear()
			self.mdb.movies.clear()
			self.myd.clear()
		except Exception as ex:
			output['result'] = 'error'
			output['message'] = str(ex)
		return json.dumps(output)

	def GET_KEY(self, key):
		output = { "result" : "success" }
		try:
			user = self.mdb.get_user(int(key))
			output["gender"] = user[0]
			output["age"] = user[1]
			output["zipcode"] = user[3]
			output["id"] = key
			output["occupation"] = user[2]
		except Exception as ex:
			output['result'] = 'error'
			output['message'] = str(ex)
		return json.dumps(output)

	def PUT(self, key):
		output = { "result" : "success" }
		the_body = cherrypy.request.body.read().decode()
		try:
			the_body = json.loads(the_body)
			user = [the_body["gender"], the_body["age"], the_body["occupation"], the_body["zipcode"]]
			if self.mdb.get_user(int(key)) == None:
				entry = {"gender": the_body["gender"], "age": the_body["age"], "zipcode": the_body["zipcode"], "result": "success", "id": uid, "occupation": the_body["occupation"]}
				self.myd["users"].append(entry)
			else:
				for entry in self.myd["users"]:
					if entry["id"] == str(key):
						entry["gender"] = the_body["gender"]
						entry["age"] = the_body["age"]
						entry["zipcode"] = the_body["zipcode"]
						entry["occupation"] = the_body["occupation"]	
			self.mdb.set_user(int(key), user)
		except Exception as ex:
			output['result'] = 'error'
			output['message'] = str(ex)
		return json.dumps(output)
	
	def DELETE_KEY(self, key):
		output = { "result" : "success" }
		try:
			for entry in self.myd["users"]:
				if entry["id"] == int(key):
					self.myd["users"].remove(entry)
			self.mdb.delete_user(int(key))
		except Exception as ex:
			output['result'] = 'error'
			output['message'] = str(ex)
		return json.dumps(output)
