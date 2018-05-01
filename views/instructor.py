from .base import BaseView

class InstructorView(BaseView):

	def __init__(self, controller):
		super().__init__(controller)

		self.set_choices([
			'Change Password',
			'Input Grades',
			'View Section Roster',
			'Logout'
		])
		
	def render(self, payload):
		self.print_title(self.get_greeting(payload['username'], payload['full_name']))
		
		print(self.get_choices_list())
		print()
		self.choice_prompt()