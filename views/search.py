from .base import BaseView

class SearchView(BaseView):

	def __init__(self, controller):
		super().__init__(controller)

		self.set_choices([
			'Back',
			'Search by Term',
			'Search by Course Name'
		])
		
	def render(self, payload):
		self.print_title('Search for Sections')

		print(self.get_choices_list())
		print()
		self.choice_prompt()