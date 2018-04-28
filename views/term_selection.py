from .base import BaseView
from utils import create_ordered_list

class TermSelectionView(BaseView):

	def __init__(self, controller):
		super().__init__(controller)

	def render(self, payload):		
		self.print_title('Select term')
		'''
			We call set_choices in here because
			the list is dynamically populated by the
			payload. The second argument are meta values
			for each choice. The meta values are sent to
			the controller along with the choice integer.
		'''
		choices = ['Back'] + payload['terms']
		choices_meta = [''] + payload['term_ids']
		self.set_choices(choices, choices_meta)

		print(self.get_choices_list())
		print()
		self.choice_prompt()