from .base import BaseView

class RegistrarView(BaseView):

	def __init__(self, controller):
		super().__init__(controller)

		self.set_choices([
			'Logout'
		])
		
	def render(self, payload):
		self.print_title('Registar')
		
		print('This is the registrar view.')
		print('Payload sent to this view:', payload)
		print()
		print(self.get_choices_list())
		print()
		self.choice_prompt()