from .base import BaseView

class RegistrarView(BaseView):

	def __init__(self, controller):
		super().__init__(controller)

		self.set_choices([
			'Change Password',
			'Register Student for Sections',
			'Logout'
		])
		
	def render(self, payload):
		self.print_title(self.get_greeting(payload['username'], payload['full_name']))
		
		print()
		print(self.get_choices_list())
		print()
		self.choice_prompt()