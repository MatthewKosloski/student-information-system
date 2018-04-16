from .base import BaseView

class MainView(BaseView):

	def __init__(self, controller):
		super().__init__(controller)

		self.set_choices([
			'Login',
			'About'
		])

	def render(self, payload):
		print()
		print()
		print('Student Information System')
		print()
		print(self.get_choices_list())
		print()

		self.choice_prompt()
