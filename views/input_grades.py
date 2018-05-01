from .base import BaseView

class InputGradesView(BaseView):

	def __init__(self, controller):
		super().__init__(controller)
		
	def render(self, payload):
		self.print_title('Input Semester Grades')

		another = 'y'
		
		while another.lower() == 'y':

			section_id = self.get_int('Section ID: ', 
				'Please provide the ID of the section to which the student belongs.')
			student_id = self.get_int('Student ID: ',
				'Please provide the ID of the student to which the grade will be given.')
			percent_grade = self.get_float_range('Percent grade: ', (0.0, 100.0))

			self.get_controller().on_details_selection(
				section_id, 
				student_id, 
				percent_grade)

			another = self.get_y_or_n('Input another student grade? (y/n): ')

		self.get_controller().go_back()
	