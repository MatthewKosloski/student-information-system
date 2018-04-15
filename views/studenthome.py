from .base import BaseView

class StudentHomeView(BaseView):

	def __init__(self, controller):
		super().__init__(controller)

		self.set_choices([
			'Logout'
		])
		
	def render(self, payload):
		print()
		print()
		print(f'Welcome, {payload.first_name} {payload.last_name}!')
		print()
		print(self.get_choices_list())
		print()
		self.choice_prompt()
