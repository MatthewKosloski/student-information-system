from .base import BaseView

class StudentIDSelectionView(BaseView):

	def __init__(self, controller):
		super().__init__(controller)
		self.__is_valid_id = False

	def set_id_status(self, status):
		self.__is_valid_id = status
		
	def render(self, payload):
		self.print_title('Select Student ID')

		while not self.__is_valid_id:

			student_id = self.get_non_empty_string('Student ID: ', 
				'Please enter the ID of a student (e.g, 5).')

			self.get_controller().on_student_id_selection(student_id)
	