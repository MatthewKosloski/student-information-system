from .base import BaseView

class StudentIDView(BaseView):

	def __init__(self, controller):
		super().__init__(controller)

	def render(self, payload):
		self.print_title('View Student Grades')
		
		student_id = input('Student ID: ')

		self.get_controller().show_student_grades(student_id)

		