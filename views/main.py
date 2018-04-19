from .base import BaseView

class MainView(BaseView):

	def __init__(self, controller):
		super().__init__(controller)

		self.set_choices([
			'Login',
			'About'
		])

	def render(self, payload):
		self.print_title('Student Information System')
		
		print(self.get_choices_list())
		print()

		self.choice_prompt()
