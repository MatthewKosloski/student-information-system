from .base import BaseView
from table import Table

class GradesView(BaseView):

	def __init__(self, controller):
		super().__init__(controller)

		self.set_choices([
			'Back'
		])

	def get_grades_table(self, grades):
		table = Table(['Course', 'Grade', 'Percent'])

		for item in grades:
			table.add_row([
				item['course'], 
				item['grade'], 
				item['percent']
			])

		return table

	def render(self, payload):
		self.print_title('Student Grades')

		print(self.get_grades_table(payload))
		print()
		print(self.get_choices_list())
		print()
		self.choice_prompt()
