from .base import BaseView

class AboutView(BaseView):

	def __init__(self, controller):
		super().__init__(controller)

		self.set_choices([
			'Back'
		])
		
	def render(self, payload):
		self.print_title('About')
		
		print('This Student Information System is made by Logan Miller,\n' +
		'Matthew Kosloski, and Paul Barnes.\n\nView the source code:\n' +
		'https://github.com/MatthewKosloski/student-information-system/')
		print()
		print(self.get_choices_list())
		print()
		self.choice_prompt()