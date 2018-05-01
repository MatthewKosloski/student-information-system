from .base import BaseController
from views import RegistrarView
from routes import *

class RegistrarController(BaseController):

	def __init__(self, router, payload):
		super().__init__(router, payload)

		self.__view = RegistrarView(self)
		self.__view.render(payload)

	'''
		Handle the user's choice and redirect
		them to the appropriate view.
		
		@param choice {int} Number corresponding to
		the view in the ordered list menu.
	'''
	def on_choice_selection(self, choice, meta):
		if choice == 1: # Logout
			self.dispatch(HOME_ROUTE)