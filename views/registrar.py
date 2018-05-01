from .base import BaseView

class RegistrarView(BaseView):

	def __init__(self, controller):
		super().__init__(controller)

		self.set_choices([
			'Change Password',
			'Logout'
		])
		
	def render(self, payload):
		self.print_title(self.get_greeting(payload['username'], payload['full_name']))
		
		print('This is the registrar view.')
		print('Payload sent to this view:', payload)
		print()
		print(self.get_choices_list())
		print()
		self.choice_prompt()