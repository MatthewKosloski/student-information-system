from .base import BaseView

class StudentView(BaseView):

	def __init__(self, controller):
		super().__init__(controller)

		self.set_choices([
			'View Profile',
			'Change Password',
			'View Grades',
			'View Schedule',
			'Search for Sections',
			'Register for Sections',
			'Logout'
		])
		
	def render(self, payload):
		self.print_title(self.get_greeting(payload['username'], payload['full_name']))
		
		print(self.get_choices_list())
		print()
		self.choice_prompt()
