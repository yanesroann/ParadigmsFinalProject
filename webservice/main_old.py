#       Abby Gervase, Grace Milton, and Roann Yanes
#       main.py -- Webservice
#       November 30, 2017

import cherrypy
import re, json
from reset import ResetController
from books import BooksController
from recommendations import RecommendationsController
from ratings import RatingsController
from years import YearsController
from genres import GenresController
from author import AuthorController
from _books_database import _books_database

def start_service():
	bdb = _books_database()
	bdb.load_books("../ooapi/book_files/books.csv")
	bdb.load_genres("../ooapi/book_files/book_tags.csv")
	booksController = BooksController(bdb=bdb)
	recommendationsController = RecommendationsController(bdb=bdb)
	ratingsController = RatingsController(bdb=bdb)
	resetController = ResetController(bdb=bdb)
	authorController = AuthorController(bdb=bdb)
	yearsController = YearsController(bdb=bdb)
	genresController = GenresController(bdb=bdb)
	dispatcher = cherrypy.dispatch.RoutesDispatcher()

	dispatcher.connect('reset_put', '/reset/', controller=resetController, action='PUT', conditions=dict(method=['PUT']))
	dispatcher.connect('books_get', '/books/', controller=booksController, action='GET', conditions=dict(method=['GET']))
	dispatcher.connect('books_post', '/books/', controller=booksController, action='POST', conditions=dict(method=['POST']))
	dispatcher.connect('books_delete', '/books/', controller=booksController, action='DELETE', conditions=dict(method=['DELETE']))
	dispatcher.connect('books_key_get', '/books/:key', controller=booksController, action='GET_KEY', conditions=dict(method=['GET']))
	dispatcher.connect('books_key_put', '/books/:key', controller=booksController, action='PUT', conditions=dict(method=['PUT']))
	dispatcher.connect('books_key_delete', '/books/:key', controller=booksController, action='DELETE_KEY', conditions=dict(method=['DELETE']))
	dispatcher.connect('recommendations_delete', '/recommendations/', controller=recommendationsController, action='DELETE', conditions=dict(method=['DELETE']))
	dispatcher.connect('recommendations_get_num', '/recommendations/:num', controller=recommendationsController, action='GET', conditions=dict(method=['GET']))
	dispatcher.connect('recommendations_post', '/recommendations/', controller=recommendationsController, action='POST', conditions=dict(method=['POST']))
	dispatcher.connect('ratings_get', '/ratings/:key', controller=ratingsController, action='GET', conditions=dict(method=['GET']))
	dispatcher.connect('author_get', '/authors/', controller=authorController, action='GET', conditions=dict(method=['GET']))
	dispatcher.connect('author_key_get', '/authors/:key', controller=authorController, action='GET_KEY', conditions=dict(method=['GET']))
	dispatcher.connect('years_get', '/years/:key', controller=yearsController, action='GET', conditions=dict(method=['GET']))
	dispatcher.connect('genres_get', '/genres/', controller=genresController, action='GET', conditions=dict(method=['GET']))
	dispatcher.connect('genres_key_get', '/genres/:key', controller=genresController, action='GET_KEY', conditions=dict(method=['GET']))


	# Configuration for the server
	conf = { 'global': {'server.socket_host': 'student04.cse.nd.edu', 'server.socket_port': 51082}, '/': {'request.dispatch': dispatcher}}

	#Starting the server 
	cherrypy.config.update(conf)
	app = cherrypy.tree.mount(None, config=conf)
	cherrypy.quickstart(app)


if __name__ == '__main__':
	start_service()
