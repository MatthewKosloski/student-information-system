from .base import BaseView
from beautifultable import BeautifulTable

class ScheduleView(BaseView):

	def __init__(self, controller):
		super().__init__(controller)

		self.set_choices([
			'Back'
		])
		
	def get_schedule_table(self, schedule):
		table = BeautifulTable()
		table.column_headers = [
			'Course', 
			'Section Number', 
			'Instructor',
			'Meet Day(s)',
			'Room',
			'Meet Time',
			'Meet Date',
			'Section Type'
		]
		table.column_alignments['Course'] = BeautifulTable.ALIGN_LEFT
		table.column_alignments['Section Number'] = BeautifulTable.ALIGN_LEFT
		table.column_alignments['Instructor'] = BeautifulTable.ALIGN_LEFT
		table.column_alignments['Meet Day(s)'] = BeautifulTable.ALIGN_LEFT
		table.column_alignments['Room'] = BeautifulTable.ALIGN_LEFT
		table.column_alignments['Meet Time'] = BeautifulTable.ALIGN_LEFT
		table.column_alignments['Meet Date'] = BeautifulTable.ALIGN_LEFT
		table.column_alignments['Section Type'] = BeautifulTable.ALIGN_LEFT

		for item in schedule:
			table.append_row([
				item['course'], 
				item['section_number'], 
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