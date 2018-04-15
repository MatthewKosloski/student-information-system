from views import MainView
from .base import BaseController

class MainController(BaseController):

	def __init__(self, params):
		super().__init__(params)

		self.__view = MainView(self)

	def index_action(self, payload):
		self.__view.render()

	def on_choice_selection(self, choice):
		if choice == 1:
			self.dispatch('/login')
		elif choice == 2:
			self.dispatch('/about')
