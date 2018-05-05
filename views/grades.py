from .base import BaseView
from table import Table

class GradesView(BaseView):

	def __init__(self, controller):
		super().__init__(controller)

		self.set_choices([
			'Back'
		])

	'''
		Creates a table listing the student's
		grades for each section.

		@param grades {list}
		@return Table
	'''
	def get_grades_table(self, grades):
		table = Table(['COURSE', 'GRADE', 'PERCENT'])

		for item in grades:
			table.add_row([
				item['course'], 
				item['grade'], 
				item['percent']
			])

		return table

	def render(self, payload):
		self.print_title(payload['view_title'])

		print(self.get_grades_table(payload['grades']))
		print()
		print(self.get_choices_list())
		print()
		self.choice_prompt()
