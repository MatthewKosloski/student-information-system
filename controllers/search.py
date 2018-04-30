from .base import BaseController
from views import SearchView
from routes import *

class SearchController(BaseController):

	def __init__(self, router, payload):
		super().__init__(router, payload)

		self.__view = SearchView(self)
		self.__view.render(payload)

	'''
		Handle the user's choice and redirect
		them to the appropriate view.
		
		@param choice {int} Number corresponding to
		the view in the ordered list menu.
	'''
	def on_choice_selection(self, choice, meta):
		if choice == 1:
			self.go_back()
		elif choice == 2:
			self.dispatch(SEARCH_SELECT_TERM_ROUTE, self.get_payload())
		elif choice == 3:
			self.dispatch(SEARCH_SELECT_NAME_ROUTE, self.get_payload())