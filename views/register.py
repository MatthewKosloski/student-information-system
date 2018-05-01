from .base import BaseView

class RegisterView(BaseView):

	def __init__(self, controller):
		super().__init__(controller)

		self.set_choices([
			'Back'
		])
		
	def render(self, payload):
		self.print_title('Register for Sections')
		
		another = 'y'

		while another.lower() == 'y':

			section_id = self.get_non_empty_string('Section ID: ', 
				'Please enter a valid section ID.')

			self.get_controller().on_id_selection(section_id, 
				payload['student_id'])

			another = self.get_y_or_n('Register for another section? (y/n): ')

		self.get_controller().go_back()