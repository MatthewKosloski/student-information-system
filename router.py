import importlib

'''
	
	Inspired by: https://github.com/daveh/php-mvc/blob/master/Core/Router.php

	A simple router class that translates
	a route (e.g., '/about') into a controller.

	Example:

	# Create a new instance of Router.
	router = Router()

	# Associate the AthleteController with the 
	# /athletes route.  Call the controller's
	# __init__ method when the route is dispatched.
	router.add('/athletes', {'controller': 'AthleteController'})

	# Create a new instance of AthleteController
	# and call it's __init__ method. The 
	# __init__ method would more than likely
	# render a view.
	router.dispatch('/atheletes')

'''
class Router():

	def __init__(self):
		self.__routes = {}
		self.__active_controller = None

	'''
		Create a new route

		@param route {str}
		@param controller {str}
	'''
	def add(self, route, controller):
		if not route in self.__routes:
			
			self.__routes[route] = {
				'controller': controller,
				'router': self
			}

	'''
		Get all the routes

		@return {dict}
	'''
	def get_routes(self):
		return self.__routes

	'''
		Remove a route
	'''
	def remove(self, route):
		if route in self.__routes:
			del self.__routes[route]

	'''
		Instantiate a new instance of
		the controller associated with
		a route.

		@param route {str}
		@param payload {dict} Data to send to
		the controller.
	'''
	def dispatch(self, route, payload = {}):
		if route in self.__routes:
			current_route = self.__routes[route]
			controller = current_route['controller']

			# Dynamically import the controller from the controller module
			controllers_module = importlib.import_module('controllers')
			controller_class = getattr(controllers_module, controller)

			self.__active_controller = controller_class(current_route, payload)
			


			