from views import AboutView
from .base import BaseController

class AboutController(BaseController):

	def __init__(self, params):
		super().__init__(params)

		self.__view = AboutView(self)

	def index_action(self, payload):
		self.__view.render()

	def on_choice_selection(self, choice):
		if choice == 1:
			self.dispatch('/')


