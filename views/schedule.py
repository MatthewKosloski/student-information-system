from .base import BaseView
from table import Table

class ScheduleView(BaseView):

	def __init__(self, controller):
		super().__init__(controller)

		self.set_choices([
			'Back'
		])
		
	def get_schedule_table(self, schedule):
		table = Table([
			'Course', 
			'Instructor',
			'Day(s)',
			'Room',
			'Meet Time',
			'Meet Date',
			'Type'
		])

		for item in schedule:
			table.add_row([
				item['course'], 
				item['instructor'],
				item['meet_day'],
				item['meet_location'],
				item['meet_time'],
				item['meet_date'],
				item['section_type']
			])
			
		return table

	def render(self, payload):
		self.print_title('Schedule')

		print(self.get_schedule_table(payload))
		print()
		print(self.get_choices_list())
		print()
		self.choice_prompt()