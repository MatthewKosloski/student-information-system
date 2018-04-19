class BaseController():

	def __init__(self, params, payload):
		self.__params = params
		self.__payload = payload

	'''
		Allows us to use router.dispatch() from
		the controller.

		@param route {str}
		@param payload {dict}
	'''
	def dispatch(self, route, payload = {}):
		return self.__params['router'].dispatch(route, payload)

	'''
		Calls dispatch with the previously used route
		and payload.
	'''
	def go_back(self):
		last_router_log_item = self.__params['router'].get_last_log_item()
		last_route = last_router_log_item['route']
		last_payload = last_router_log_item['payload']

		self.__params['router'].dispatch(last_route, last_payload) 

	'''
		Returns the payload provided
		to the controller.

		@return {dict}
	'''
	def get_payload(self):
		return self.__payload
