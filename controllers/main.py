from views import MainView
from routes import LOGIN_ROUTE, ABOUT_ROUTE
from .base import BaseController

class MainController(BaseController):

	def __init__(self, params, payload):
		super().__init__(params, payload)

		self.__view = MainView(self)
		self.__view.render(payload)

	'''
		Handle the user's choice and redirect
		them to the appropriate view.
		
		@param choice {int} Number corresponding to
		the view in the ordered list menu.
	'''
	def on_choice_selection(self, choice):
		if choice == 1:
			self.dispatch(LOGIN_ROUTE)
		elif choice == 2:
			self.dispatch(ABOUT_ROUTE)
