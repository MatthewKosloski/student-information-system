from views import StudentHomeView
from .base import BaseController

class StudentHomeController(BaseController):

	def __init__(self, params):
		super().__init__(params)

		self.__view = StudentHomeView(self)

	def index_action(self, payload):
		self.__view.render(payload)

	def on_choice_selection(self, choice):
		if choice == 1:
			self.dispatch('/')


