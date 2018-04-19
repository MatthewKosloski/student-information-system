from .base import BaseController
from views import StudentView
from models import Student
from routes import (
	STUDENT_PROFILE_ROUTE, 
	CHANGE_PASSWORD_ROUTE, 
	STUDENT_GRADES_ROUTE, 
	HOME_ROUTE
)

class StudentController(BaseController):

	def __init__(self, params, payload):
		super().__init__(params, payload)

		self.__view = StudentView(self)

		self.__view.render(self.get_username_and_full_name(payload))

	'''
		Get the username, firstname, and lastname
		from the student whose ID is the one provided.

		@param id {int} ID of the student
		@return {dict} A dictionary containing the username
		and full name of the user to be displayed in the
		student view.
	'''
	def get_username_and_full_name(self, id):
		try:
			query = (Student
				.select(Student.username, 
					Student.first_name, 
					Student.last_name)
				.where(Student.id == id)
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
	def on_choice_selection(self, choice):
		student_id = self.get_payload()
		if choice == 1: # View Profile
			# specify type so we can reuse profile module
			self.dispatch(STUDENT_PROFILE_ROUTE, {'type': 'student', 'id': student_id})
		elif choice == 2: # Change Password
		# specify type so we can reuse password module
			self.dispatch(CHANGE_PASSWORD_ROUTE, {'type': 'student', 'id': student_id})
		elif choice == 3:
			self.dispatch(STUDENT_GRADES_ROUTE, student_id)
		elif choice == 4: # Logout
			self.dispatch(HOME_ROUTE)


