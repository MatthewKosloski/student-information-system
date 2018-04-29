from .base import BaseView

class InstructorView(BaseView):

	def __init__(self, controller):
		super().__init__(controller)

		self.set_choices([
			'Back'
		])
		
	def render(self, payload):
		self.print_title('Instructor View')
		
		print('Payload:', payload)
		print()
		print(self.get_choices_list())
		print()
		self.choice_prompt()