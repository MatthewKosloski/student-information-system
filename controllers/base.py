from routes import *
from account_types import *

class BaseController():

	def __init__(self, router, payload):
		self.__router = router
		self.__payload = payload

	'''
		Allows us to use router.dispatch() from
		the controller.

		@param route {str}
		@param payload {dict}
	'''
	def dispatch(self, route, payload = {}):
		return self.__router.dispatch(route, payload)

	'''
		Calls dispatch with the previously used route
		and payload.
	'''
	def go_back(self):
		last_router_log_item = self.__router.get_last_log_item()
		last_route = last_router_log_item['route']
		last_payload = last_router_log_item['payload']

		self.__router.dispatch(last_route, last_payload) 

	'''
		Takes the user to their splash page.
	'''
	def go_home(self):
		account_type = self.__payload['type']
		payload = {'id': self.get_payload()['id']}

		if account_type == STUDENT_ACCOUNT_TYPE:
			self.dispatch(STUDENT_ROUTE, payload)
		elif account_type == INSTRUCTOR_ACCOUNT_TYPE:
			self.dispatch(INSTRUCTOR_ROUTE, payload)
		elif account_type == REGISTRAR_ACCOUNT_TYPE:
			self.dispatch(REGISTRAR_ROUTE, payload)

	'''
		Returns the payload provided
		to the controller.

		@return {dict}
	'''
	def get_payload(self):
		return self.__payload

	'''
		Returns the route with which
		the controller was instantiated.

		@return {str}
	'''
	def get_route(self):
		return self.__payload['__route']

	'''
		Returns the parts of the route
		as a tuple.
		
		@return {tuple}
	'''
	def get_route_parts(self):
		return tuple(self.__payload['__route'].split('/'))
