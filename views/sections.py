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

		@param sections {list}
	'''
	def get_sections_table(self, sections):
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

		for item in sections:
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

		if len(payload['sections']) != 0:
			print(self.get_sections_table(payload['sections']))
		else:
			print(f'There are no sections for {payload["course_name"]}.')

		print()
		print(self.get_choices_list())
		print()
		self.choice_prompt()