from .base import BaseView

class AboutView(BaseView):

	def __init__(self, controller):
		super().__init__(controller)

		self.set_choices([
			'Back'
		])
		
	def render(self):
		print()
		print()
		print('About')
		print()
		print(self.get_choices_list())
		print()
		print('This is the about view.')
		print()

		self.choice_prompt()
