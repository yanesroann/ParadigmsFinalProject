#       Abby Gervase, Grace Milton, and Roann Yanes
#       books.py -- Webservice
#       November 30, 2017

import cherrypy
import re, json
from _books_database import _books_database

class BooksController(object):
    def __init__(self, bdb=None):
        self.bdb = bdb
        self.myd = {}
        self.myd['books'] = []
        # Stores all books and their data in a dictionary
        for bid in bdb.books:
            entry = { "result" : "success" }
            entry["authors"] = bdb.books[bid][0]
            entry["title"] = bdb.books[bid][2]
            entry["year"] = bdb.books[bid][1]
            entry["id"] = bid
            if bid in bdb.images and bdb.images[bid]:
                entry["img"] = bdb.images[bid]
            else:
                entry["img"] = "no_image.jpg"
            self.myd["books"].append(entry)

    # Retrieves dictionary with all books and their data
    def GET(self):
        output = {}
        try:
            output = self.myd
            # Reloads book dictionary in case books have been added or deleted
            self.myd['books'] = []
            for bid in self.bdb.books:
                entry = { "result" : "success" }
                entry["authors"] = self.bdb.books[bid][0]
                entry["title"] = self.bdb.books[bid][2]
                entry["year"] = self.bdb.books[bid][1]
                entry["id"] = bid
                if bid in self.bdb.images and self.bdb.images[bid]:
                    entry["img"] = self.bdb.images[bid]
                else:
                    entry["img"] = "no_image.jpg"
                self.myd["books"].append(entry)
            output["result"] = "success"
        except Exception as ex:
            output['result'] = 'error'
            output['message'] = str(ex)
        return json.dumps(output)

    # Adds book to dictionary
    def POST(self):
        output = { "result" : "success" }
        the_body = cherrypy.request.body.read().decode()
        try:
            the_body = json.loads(the_body)
            book = [the_body["authors"], the_body["year"], the_body["title"]]
            found = False
            for bid in self.bdb.books: # if this is already a book
                if book == self.bdb.books[bid]:
                    found = True
            if not found:
                bid = len(self.bdb.books) + 1
            while bid in self.bdb.books:
                bid += 1 # keep adding one to bid
            self.bdb.set_book(bid, book)
            self.bdb.set_image(bid, "no_image.jpg")
            entry = {"authors": the_body["authors"], "title": the_body["title"], "year": the_body["year"], "id": bid, "img": "no_image.jpg", "result": "success"}
            self.myd["books"].append(entry)
            output["id"] = bid
        except Exception as ex:
            output['result'] = 'error'
            output['message'] = str(ex)
        return json.dumps(output)

    # Deletes all books and data
    def DELETE(self):
        output = { "result" : "success" }
        try:
            self.bdb.authors.clear()
            self.bdb.images.clear()
            self.bdb.ratings.clear()
            self.bdb.books.clear()
            self.bdb.voted_books.clear()
            self.bdb.recommendations.clear()
            self.bdb.genres.clear()
            self.myd.clear()
        except Exception as ex:
            output['result'] = 'error'
            output['message'] = str(ex)
        return json.dumps(output)

    # Retrieves information for individual book
    def GET_KEY(self, key):
        output = { "result" : "success" }
        try:
            book = self.bdb.get_book(int(key))
            output["authors"] = book[0]
            output["title"] = book[2]
            output["year"] = book[1]
            image = self.bdb.get_image(int(key))
            if image:
                output["img"] = image
            else:
                output["img"] = "no_image.jpg"
            output["id"] = key
        except Exception as ex:
            output['result'] = 'error'
            output['message'] = str(ex)
        return json.dumps(output)

    # Updates information for book
    def PUT(self, key):
        output = { "result" : "success" }
        the_body = cherrypy.request.body.read().decode()
        try:
            the_body = json.loads(the_body)
            book = [the_body["authors"], the_body["year"], the_body["title"]]
            # If book does not exist, adds book
            if self.bdb.get_book(int(key)) == None:
                self.bdb.set_image(int(key), "no_image.jpg")
                entry = {"authors": the_body["authors"], "year": the_body["year"], "title": the_body["title"], "result": "success", "id": key, "img": "no_image.jpg"}
                self.myd["books"].append(entry)
            else:
                for entry in self.myd["books"]:
                    if entry["id"] == str(key):
                        entry["authors"] = the_body["authors"]
                        entry["year"] = the_body["year"]	
                        entry["title"] = the_body["title"]	
            self.bdb.set_book(int(key), book)
        except Exception as ex:
            output['result'] = 'error'
            output['message'] = str(ex)
        return json.dumps(output)

    # Deletes individual book
    def DELETE_KEY(self, key):
        output = { "result" : "success" }
        try:
            for entry in self.myd["books"]:
                if entry["id"] == int(key):
                    self.myd["books"].remove(entry)
            self.bdb.delete_book(int(key))
        except Exception as ex:
            output['result'] = 'error'
            output['message'] = str(ex)
        return json.dumps(output)
