from views import ScheduleView
from .base import BaseController

class ScheduleController(BaseController):

	def __init__(self, router, payload):
		super().__init__(router, payload)

		self.__view = ScheduleView(self)
		self.__view.render(payload)

	'''
		Handle the user's choice and redirect
		them to the appropriate view.
		
		@param choice {int} Number corresponding to
		the view in the ordered list menu.
	'''
	def on_choice_selection(self, choice):
		if choice == 1:
			self.go_back()