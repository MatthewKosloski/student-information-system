class BaseController():

	def __init__(self, params, payload):
		self.__params = params
		self.__payload = payload

	# Syntactic sugar for self.__params['router'].dispatch
	def dispatch(self, route, payload = {}):
		return self.__params['router'].dispatch(route, payload)

	def get_payload(self):
		return self.__payload
