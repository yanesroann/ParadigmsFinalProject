# Abby Gervase, Grace Milton, Roann Yanes
# author.py

import cherrypy
import re, json
from _books_database import _books_database

class AuthorController(object):
    def __init__(self, bdb=None):
        self.bdb = bdb
        self.myd = {}
        self.myd["authors"] = []
        for author in self.bdb.author_ids:
            entry = { "result" : "success" }
            aid = self.bdb.author_ids[author]
            entry["author"] = author
            entry["books"] = list(self.bdb.authors[aid])
            entry["id"] = aid
            self.myd["authors"].append(entry)
			
    def GET(self):
        output = {}
        try:
            output = self.myd
            self.myd["authors"] = []
            for author in self.bdb.author_ids:
                entry = { "result" : "success" }
                aid = self.bdb.author_ids[author]
                entry["author"] = author
                entry["books"] = list(self.bdb.authors[aid])
                entry["id"] = aid
                self.myd["authors"].append(entry)
            output["result"] = "success"
        except Exception as ex:
            output['result'] = 'error'
            output['message'] = str(ex)
        return json.dumps(output)


    def GET_KEY(self, key):
        output = {"result" : "success"}
        try:
            books = list(self.bdb.authors[int(key)])
            output["books"] = books
            output["author"] = int(key)
        except Exception as ex:
            output['result'] = 'error'
            output['message'] = str(ex)
        return json.dumps(output)
