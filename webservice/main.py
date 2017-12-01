# Roann Yanes 

import cherrypy
import re, json
#from reset import ResetController
from books import BooksController
#from users import UsersController
#from recommendations import RecommendationsController
#from ratings import RatingsController
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
	#mdb.load_ratings("/home/paradigms/ml-1m/ratings.dat")
	#mdb.load_images("/home/paradigms/images.dat")
	booksController = BooksController(bdb=bdb)
	#usersController = UsersController(mdb=mdb)
	#recommendationsController = RecommendationsController(mdb=mdb)
	#ratingsController = RatingsController(mdb=mdb)
	#resetController = ResetController(mdb=mdb)
	optionsController = OptionsController(bdb=bdb)
	dispatcher = cherrypy.dispatch.RoutesDispatcher()

#	dispatcher.connect('reset_put', '/reset/', controller=resetController, action='PUT', conditions=dict(method=['PUT']))
#	dispatcher.connect('reset_put_key', '/reset/:key', controller=resetController, action='PUT_KEY', conditions=dict(method=['PUT']))
	dispatcher.connect('books_get', '/books/', controller=booksController, action='GET', conditions=dict(method=['GET']))
	dispatcher.connect('books_post', '/books/', controller=booksController, action='POST', conditions=dict(method=['POST']))
#	dispatcher.connect('movies_delete', '/movies/', controller=moviesController, action='DELETE', conditions=dict(method=['DELETE']))
#	dispatcher.connect('movies_key_get', '/movies/:key', controller=moviesController, action='GET_KEY', conditions=dict(method=['GET']))
#	dispatcher.connect('movies_key_put', '/movies/:key', controller=moviesController, action='PUT', conditions=dict(method=['PUT']))
#	dispatcher.connect('movies_key_delete', '/movies/:key', controller=moviesController, action='DELETE_KEY', conditions=dict(method=['DELETE']))
#	dispatcher.connect('users_get', '/users/', controller=usersController, action='GET', conditions=dict(method=['GET']))
#	dispatcher.connect('users_post', '/users/', controller=usersController, action='POST', conditions=dict(method=['POST']))
#	dispatcher.connect('users_delete', '/users/', controller=usersController, action='DELETE', conditions=dict(method=['DELETE']))
#	dispatcher.connect('users_key_get', '/users/:key', controller=usersController, action='GET_KEY', conditions=dict(method=['GET']))
#	dispatcher.connect('users_put', '/users/:key', controller=usersController, action='PUT', conditions=dict(method=['PUT']))
#	dispatcher.connect('users_key_delete', '/users/:key', controller=usersController, action='DELETE_KEY', conditions=dict(method=['DELETE']))
#	dispatcher.connect('recommendations_delete', '/recommendations/', controller=recommendationsController, action='DELETE', conditions=dict(method=['DELETE']))
#	dispatcher.connect('recommendations_get_key', '/recommendations/:key', controller=recommendationsController, action='GET', conditions=dict(method=['GET']))
#	dispatcher.connect('recommendations_put_key', '/recommendations/:key', controller=recommendationsController, action='PUT', conditions=dict(method=['PUT']))
#	dispatcher.connect('ratings_get', '/ratings/:key', controller=ratingsController, action='GET', conditions=dict(method=['GET']))

#	dispatcher.connect('reset_put_options', '/reset/', controller=optionsController, action='OPTIONS', conditions=dict(method=['OPTIONS']))
#	dispatcher.connect('reset_put_key_options', '/reset/:key', controller=optionsController, action='OPTIONS', conditions=dict(method=['OPTIONS']))
#	dispatcher.connect('movies_options', '/movies/', controller=optionsController, action='OPTIONS', conditions=dict(method=['OPTIONS']))
#	dispatcher.connect('movies_key_options', '/movies/:key', controller=optionsController, action='OPTIONS', conditions=dict(method=['OPTIONS']))
#	dispatcher.connect('users_options', '/users/', controller=optionsController, action='OPTIONS', conditions=dict(method=['OPTIONS']))
#	dispatcher.connect('users_key_options', '/users/:key', controller=optionsController, action='OPTIONS', conditions=dict(method=['OPTIONS']))
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
