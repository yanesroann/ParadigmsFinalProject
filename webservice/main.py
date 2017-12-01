# Roann Yanes 

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


#def CORS():
#	cherrypy.response.headers["Access-Control-Allow-Origin"] = "*"
#	cherrypy.response.headers["Access-Control-Allow-Methods"] = "GET, PUT, POST, DELETE"
#	cherrypy.response.headers["Access-Control-Allow-Credentials"] = "*"

class OptionsController(object):
	def __init__(self, bdb=None):
		self.bdb = bdb
	def OPTIONS(self, *args, **kargs):
		return ""

def start_service():
	bdb = _books_database()
	bdb.load_books("../ooapi/book_files/books.csv")
	bdb.load_genres("../ooapi/book_files/book_tags.csv")
	#bdb.load_ratings("/home/paradigms/ml-1m/ratings.dat")
	#bdb.load_images("/home/paradigms/images.dat")
	booksController = BooksController(bdb=bdb)
	recommendationsController = RecommendationsController(bdb=bdb)
	ratingsController = RatingsController(bdb=bdb)
	resetController = ResetController(bdb=bdb)
	authorController = AuthorController(bdb=bdb)
	yearsController = YearsController(bdb=bdb)
	genresController = GenresController(bdb=bdb)
	optionsController = OptionsController(bdb=bdb)
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

#	dispatcher.connect('reset_put_options', '/reset/', controller=optionsController, action='OPTIONS', conditions=dict(method=['OPTIONS']))
#	dispatcher.connect('reset_put_key_options', '/reset/:key', controller=optionsController, action='OPTIONS', conditions=dict(method=['OPTIONS']))
#	dispatcher.connect('books_options', '/books/', controller=optionsController, action='OPTIONS', conditions=dict(method=['OPTIONS']))
#	dispatcher.connect('books_key_options', '/books/:key', controller=optionsController, action='OPTIONS', conditions=dict(method=['OPTIONS']))
#	dispatcher.connect('recommendations_options', '/recommendations/', controller=optionsController, action='OPTIONS', conditions=dict(method=['OPTIONS']))
#	dispatcher.connect('recommendations_key_options', '/recommendations/:key', controller=optionsController, action='OPTIONS', conditions=dict(method=['OPTIONS']))
#	dispatcher.connect('ratings_options', '/ratings/:key', controller=optionsController, action='OPTIONS', conditions=dict(method=['OPTIONS']))

	# configuration for the server
	conf = { 'global': {'server.socket_host': 'student04.cse.nd.edu', 'server.socket_port': 51082}, '/': {'request.dispatch': dispatcher}}
	#conf = { 'global': {'server.socket_host': 'student04.cse.nd.edu', 'server.socket_port': 51082}, '/': {'request.dispatch': dispatcher, 'tools.CORS.on' : True }}

	#starting the server 
	cherrypy.config.update(conf)
	app = cherrypy.tree.mount(None, config=conf)
	cherrypy.quickstart(app)


if __name__ == '__main__':
	#cherrypy.tools.CORS = cherrypy.Tool('before_finalize', CORS)
	start_service()
