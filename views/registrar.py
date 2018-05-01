from .base import BaseView

class RegistrarView(BaseView):

	def __init__(self, controller):
		super().__init__(controller)

		self.set_choices([
			'View Profile',
			'View Student',
			'Logout'
		])
		
	def render(self, payload):
		print()
		print(f'Welcome, {payload["username"]} ({payload["full_name"]})!')
		print()
		print(self.get_choices_list())
		print()
		self.choice_prompt()
