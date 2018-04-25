from views import InstructorStudentGradesView
from .base import BaseController
from routes import *

class InstructorStudentGradesController(BaseController):

	def __init__(self, router, payload):
		super().__init__(router, payload)

		self.__view = InstructorStudentGradesView(self)
		self.__view.render(payload)

	def show_student_grades(self, student_id):
		self.dispatch(STUDENT_GRADES_ROUTE, student_id)