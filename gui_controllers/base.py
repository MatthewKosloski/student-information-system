
class BaseController():

	def __init__(self, router, root, payload):
		self.__router = router
		self.__root = root
		self.__payload = payload

	def dispatch(self, route, payload = {}):
		return self.__router.dispatch(route, payload)

	def go_back(self):
		last_router_log_item = self.__router.get_last_log_item()
		last_route = last_router_log_item['route']
		last_payload = last_router_log_item['payload']

		self.__router.dispatch(last_route, last_payload) 

	def get_root(self):
		return self.__root
