import importlib

'''
	
	Inspired by: https://github.com/daveh/php-mvc/blob/master/Core/Router.php

	A simple router class that translates
	a route (e.g., '/about') into a controller
	and action.  An action is just a method
	on the controller that we wish to call upon
	the initialization of the controller.

	Example:

	# Create a new instance of Router.
	router = Router()

	# Associate the AthleteController with the 
	# /athletes route.  Call the controller's
	# index_action when the route is dispatched.

	router.add('/athletes', {
		'controller': 'AthleteController', 
		'action': 'index_action'
	})

	# Create a new instance of AthleteController
	# and call it's index_action method. The 
	# index_action method would more than likely
	# render a view.
	router.dispatch('/atheletes')

'''
class Router():

	def __init__(self):
		self.__routes = {}

	'''
		Create a new route
	'''
	def add(self, route, params = {}):
		if not route in self.__routes:
			
			'''
				Add the router instance to the params
				so the controller can use it
			'''
			params['router'] = self

			self.__routes[route] = params

	'''
		Get all the routes
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
		Call the action on the controller
		of the route.
	'''
	def dispatch(self, route, payload = {}):
		if route in self.__routes:
			current_route = self.__routes[route]
			controller = current_route['controller'] # 'FooController'
			action = current_route['action'] # 'index_action'

			# from controllers import FooController
			controllers_module = importlib.import_module('controllers')
			controller_class = getattr(controllers_module, controller)
			controller_obj = controller_class(current_route) # foo_controller = FooController()
			controller_action = getattr(controller_obj, action) # foo_controller.index_action()

			controller_action(payload)


			