from .base import BaseController
from views import InstructorView
from models import Instructor
from common_queries import get_username_and_full_name
from account_types import INSTRUCTOR_ACCOUNT_TYPE
from routes import *

class InstructorController(BaseController):

	def __init__(self, router, payload):
		super().__init__(router, payload)

		self.__view = InstructorView(self)

		try:
			self.__view.render(get_username_and_full_name(Instructor, payload['id']))
		except ValueError as e:
			self.__view.print_message(e)

	'''
		Handle the user's choice and redirect
		them to the appropriate view.
		
		@param choice {int} Number corresponding to
		the view in the ordered list menu.

		@param meta {any} Any data associated with
		the choice number. This is set in the 2nd
		(optional) argument to set_choices in the view.
		Can be used to provide some info to dynamic list items.
	'''
	def on_choice_selection(self, choice, meta):
		instructor_id = self.get_payload()['id']
		
		instructor_payload = {'type': INSTRUCTOR_ACCOUNT_TYPE, 'id': instructor_id}

		if choice == 1: # Change Password
			self.dispatch(CHANGE_PASSWORD_ROUTE, instructor_payload)
		elif choice == 2: # Input Grades
			self.dispatch(INSTRUCTOR_INPUT_GRADES_ROUTE, instructor_payload)
		elif choice == 3: # View Section Roster
			self.dispatch(INSTRUCTOR_ROSTER_SELECT_TERM_ROUTE, instructor_payload)
		elif choice == 4: # Logout
			self.dispatch(HOME_ROUTE)




