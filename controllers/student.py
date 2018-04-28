from .base import BaseController
from views import StudentView
from models import Student
from routes import *

class StudentController(BaseController):

	def __init__(self, router, payload):
		super().__init__(router, payload)

		self.__view = StudentView(self)

		self.__view.render(self.get_username_and_full_name())

	'''
		Get the username, firstname, and lastname
		from the student whose ID is the one provided.

		@param id {int} ID of the student
		@return {dict} A dictionary containing the username
		and full name of the user to be displayed in the
		student view.
	'''
	def get_username_and_full_name(self):
		student_id = self.get_payload()['id']
		try:
			query = (Student
				.select(Student.username, 
					Student.first_name, 
					Student.last_name)
				.where(Student.id == student_id)
				.get())

			return {
				'username': query.username,
				'full_name': f'{query.first_name} {query.last_name}'
			}
		except DoesNotExist:
			self.__view.print_message('Student does not exist.')

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
		elif choice == 5: # Logout
			self.dispatch(HOME_ROUTE)
		else:
			self.dispatch(HOME_ROUTE)

