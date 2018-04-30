from .base import BaseView

class NameSelectionView(BaseView):

	def __init__(self, controller):
		super().__init__(controller)
		self.__is_valid_name = False

	def set_name_status(self, status):
		self.__is_valid_name = status
		
	def render(self, payload):
		self.print_title(
			'Search by Course Name',
			'Browse sections by a course name (e.g., CPSC-3310).'
		)
		
		while not self.__is_valid_name:

			name = self.get_non_empty_string('Course name: ', 
				'Please enter the name of a course (e.g, CPSC-3310).')

			self.get_controller().on_name_selection(name)
	