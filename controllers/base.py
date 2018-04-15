class BaseController():

	def __init__(self, params):
		self.__params = params

	# Syntactic sugar for self.__params['router'].dispatch
	def dispatch(self, route, payload = {}):
		return self.__params['router'].dispatch(route, payload)
