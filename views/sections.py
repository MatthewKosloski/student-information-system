from .base import BaseView
from table import Table

class SectionsView(BaseView):

	def __init__(self, controller):
		super().__init__(controller)

		self.set_choices([
			'Home',
			'Back'
		])
		
	'''
		Displays a table of sections.

		@param schedule {dict}
	'''
	def get_sections_table(self, schedule):
		table = Table([
			'COURSE', 
			'TERM',
			'INSTRUCTOR',
			'DAY(S)',
			'ROOM',
			'MEET TIME',
			'MEET DATE',
			'TYPE'
		])

		for item in schedule:
			table.add_row([
				item['course'], 
				item['term'],
				item['instructor'],
				item['meet_day'],
				item['meet_location'],
				item['meet_time'],
				item['meet_date'],
				item['section_type']
			])
			
		return table

	def render(self, payload):
		self.print_title(payload['view_title'])

		print(self.get_sections_table(payload['sections']))
		print()
		print(self.get_choices_list())
		print()
		self.choice_prompt()