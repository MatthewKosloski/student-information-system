from views import InstructorView
from .base import BaseController
from routes import *
class InstructorController(BaseController):

	def __init__(self, router, payload):
		super().__init__(router, payload)

		self.__view = InstructorView(self)
		self.__view.render(payload)

	'''
		Handle the user's choice and redirect
		them to the appropriate view.
		
		@param choice {int} Number corresponding to
		the view in the ordered list menu.
	'''
	def on_choice_selection(self, choice):
		instructor_id = self.get_payload()
		if choice == 1:
			self.dispatch(INSTRUCTOR_PROFILE_ROUTE, {'type': 'instructor', 'id': instructor_id})
		elif choice == 2:
			self.dispatch(CHANGE_PASSWORD_ROUTE, {'type': 'instructor', 'id': instructor_id})
		elif choice == 3:
			self.dispatch(INSTRUCTOR_INPUT_GRADES_ROUTE)
		elif choice == 4:
			self.dispatch(INSTRUCTOR_SCHEDULE_ROUTE)
		elif choice == 5:
			self.dispatch(INSTRUCTOR_STUDENT_GRADES_ROUTE)