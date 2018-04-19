class BaseController():

	def __init__(self, params, payload):
		self.__params = params
		self.__payload = payload

	# Syntactic sugar for self.__params['router'].dispatch
	def dispatch(self, route, payload = {}):
		return self.__params['router'].dispatch(route, payload)

	def get_router_log(self):
		return self.__params['router'].get_log()

	'''
		Calls dispatch with the previously used route
		and payload.
	'''
	def go_back(self):
		last_router_log_item = self.__params['router'].get_last_log_item()
		last_route = last_router_log_item['route']
		last_payload = last_router_log_item['payload']

		self.__params['router'].dispatch(last_route, last_payload) 

	def get_payload(self):
		return self.__payload
