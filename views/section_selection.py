from .base import BaseView

class SectionSelectionView(BaseView):

	def __init__(self, controller):
		super().__init__(controller)

	def render(self, payload):		
		self.print_title('Select section')
		'''
			We call set_choices in here because
			the list is dynamically populated by the
			payload. The second argument are meta values
			for each choice. The meta values are sent to
			the controller along with the choice integer.
		'''
		choices = ['Home', 'Back'] + payload['sections']
		choices_meta = ['', ''] + payload['section_ids']
		self.set_choices(choices, choices_meta)

		print(self.get_choices_list())
		print()
		self.choice_prompt()