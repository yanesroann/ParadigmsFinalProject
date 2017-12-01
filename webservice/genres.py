# Abby Gervase, Grace Milton, Roann Yanes
# genres.py

import cherrypy
import re, json
from _books_database import _books_database

class GenresController(object):
    def __init__(self, bdb=None):
        self.bdb = bdb
        self.myd = {}
        self.myd["genres"] = []
        for genre in self.bdb.genres:
            entry = { "result" : "success" }
            entry["genre"] = genre
            entry["books"] = list(self.bdb.genres[genre])
            self.myd["genres"].append(entry)
			
    def GET(self):
        output = {}
        try:
            output = self.myd
            self.myd["genres"] = []
            for genre in self.bdb.genres:
                entry = { "result" : "success" }
                entry["genre"] = genre
                entry["books"] = list(self.bdb.genres[genre])
                self.myd["genres"].append(entry)
            output["result"] = "success"
        except Exception as ex:
            output['result'] = 'error'
            output['message'] = str(ex)
        return json.dumps(output)


    def GET_KEY(self, key):
        output = {"result" : "success"}
        try:
            books = list(self.bdb.genres[int(key)])
            output["books"] = books
            output["genre"] = int(key)
        except Exception as ex:
            output['result'] = 'error'
            output['message'] = str(ex)
        return json.dumps(output)
