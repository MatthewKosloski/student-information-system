from .base import BaseView
from table import Table

class RosterView(BaseView):

	def __init__(self, controller):
		super().__init__(controller)

		self.set_choices([
			'Back'
		])

	'''
		Creates a table from the data
		in the payload.

		@param students {dict}
		@return table {Table}
	'''
	def get_roster_table(self, students):
		table = Table([
			'LAST NAME', 
			'FIRST NAME', 
			'ID', 
			'LETTER GRADE', 
			'PERCENT GRADE'])

		for student in students:

			table.add_row([
				student['last_name'], 
				student['first_name'], 
				student['id'],
				student['letter_grade'],
				student['percent_grade']])

		return table
		
	def render(self, payload):
		self.print_title(payload['view_title'])
		
		print(self.get_roster_table(payload['roster']))
		print(self.get_choices_list())
		print()

		self.choice_prompt()