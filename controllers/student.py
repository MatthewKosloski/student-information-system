from .base import BaseController
from views import StudentView
from models import Student
from common_queries import get_username_and_full_name
from routes import *

class StudentController(BaseController):

	def __init__(self, router, payload):
		super().__init__(router, payload)

		self.__view = StudentView(self)

		try:
			self.__view.render(get_username_and_full_name(Student, payload['id']))
		except ValueError as e:
			self.__view.print_message(e)

	'''
		Handle the user's choice and redirect
		them to the appropriate view.
		
		@param choice {int} Number corresponding to
		the view in the ordered list menu.
	'''
	def on_choice_selection(self, choice, meta):
		student_id = self.get_payload()['id']

		student_payload = {'type': 'student', 'id': student_id}

		if choice == 1: # View Profile
			self.dispatch(STUDENT_PROFILE_ROUTE, student_payload)
		elif choice == 2: # Change Password
			self.dispatch(CHANGE_PASSWORD_ROUTE, student_payload)
		elif choice == 3: # Student grades
			self.dispatch(STUDENT_GRADES_SELECT_TERM_ROUTE, student_payload)
		elif choice == 4: # Student schedule
			self.dispatch(STUDENT_SCHEDULE_SELECT_TERM_ROUTE, student_payload)
		elif choice == 5: # Search for Sections
			self.dispatch(SEARCH_ROUTE)
		elif choice == 6: # Register for Sections
			self.dispatch(STUDENT_REGISTER_ROUTE, {'student_id': student_id})
		elif choice == 7: # Logout
			self.dispatch(HOME_ROUTE)
		else:
			self.dispatch(HOME_ROUTE)

