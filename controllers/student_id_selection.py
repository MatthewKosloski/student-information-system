from .base import BaseController
from views import StudentIDSelectionView
from models import Student
from routes import *

class StudentIDSelectionController(BaseController):

	def __init__(self, router, payload):
		super().__init__(router, payload)

		self.__view = StudentIDSelectionView(self)
		self.__view.render(payload)

	'''
		Returns a boolean indicating if
		a Student exists with the provided
		ID.

		@param id {int}
		@return {bool}
	'''
	def is_valid_student_id(self, id):
		query = (Student
			.select()
			.where(Student.id == id))
		return query.exists()

	'''
		Takes the inputted student ID
		and navigates the user to the 
		appropriate view.
		
		@param student_id {int}
	'''
	def on_student_id_selection(self, student_id):
		if self.is_valid_student_id(int(student_id)):
			self.__view.set_id_status(True)
			payload = {
				'type': self.get_payload()['type'],
				'id': self.get_payload()['id'],
				'student_id': student_id
			}
			if self.get_route() == REGISTRAR_REGISTER_STUDENT_SELECT_ID_ROUTE:
				self.dispatch(REGISTRAR_REGISTER_STUDENT_ROUTE, payload)
				self.go_home()
		else:
			self.__view.print_message(f'No student with an ID of {student_id} exists.')




