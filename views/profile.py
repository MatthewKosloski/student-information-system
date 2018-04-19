from .base import BaseView

class ProfileView(BaseView):

	def __init__(self, controller):
		super().__init__(controller)

		self.set_choices([
			'Back'
		])
		
	def render(self, payload):
		self.print_title(f'Profile of {payload["full_name"]}')
		
		print('ID:', payload['id'])
		print('Username:', payload['username'])
		print('First Name:', payload['first_name'])
		print('Last Name:', payload['last_name'])
		print('Full Name:', payload['full_name'])
		print()
		print(self.get_choices_list())
		print()

		self.choice_prompt()
