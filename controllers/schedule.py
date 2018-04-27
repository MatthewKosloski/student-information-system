from .base import BaseController
from views import ScheduleView
from routes import HOME_ROUTE
from models import Student, Registration, Course, Section, Instructor

class ScheduleController(BaseController):

	def __init__(self, router, payload):
		super().__init__(router, payload)

		self.__view = ScheduleView(self)
		self.__view.render(self.get_student_schedule())

	'''
		Determine which model to use for queries
		based on the "type" key found in
		the payload.

		@return {Model}
	'''
	def get_model(self):
		account_type = self.get_payload()['type']
		if account_type == 'student':
			return Student

	def get_student_schedule(self):
		student_id = self.get_payload()['id']
		query = (Registration
			.select(Course.name,
				Course.title, 
				Section.number, 
				Instructor.first_name, 
				Instructor.last_name, 
				Section.meet_day, 
				Section.meet_location, 
				Section.meet_time_start, 
				Section.meet_time_end, 
				Section.start_date, 
				Section.end_date, 
				Section.type)
			.join(Section, on=(Registration.section_id == Section.id))
			.join(Course, on=(Section.course_id == Course.id))
			.join(Instructor, on=(Section.instructor_id == Instructor.id))
			.where(Registration.student_id == student_id)
			.dicts())

		return self.simplify_student_schedule(query)

	def simplify_student_schedule(self, schedule):
		simplified_schedule = []
		for item in schedule:
			simplified_schedule.append({
				'meet_day': self.get_meet_day(item['meet_day']),
				'meet_time': self.get_meet_time(item['meet_time_start'], item['meet_time_end']),
				'meet_date': self.get_meet_date(item['start_date'], item['end_date']),
				'section_type': self.get_section_type(item['type']),
				'course': f'{item["name"]} {item["title"]}',
				'instructor': f'{item["first_name"]} {item["last_name"]}',
				'section_number': item['number'],
				'meet_location': item['meet_location']
			})
		return simplified_schedule

	def get_meet_time(self, meet_time_start, meet_time_end):
		start = self.get_hour_minute(meet_time_start)
		end = self.get_hour_minute(meet_time_end)

		start_formatted = f'{start[0]}:{start[1]}'
		end_formatted = f'{end[0]}:{end[1]}'

		return f'{start_formatted}-{end_formatted}'

	def get_meet_date(self, start_date, end_date):
		start = self.get_year_month_day(start_date)
		end = self.get_year_month_day(end_date)

		start_formatted = f'{start[0]}/{start[1]}/{start[2]}'
		end_formated = f'{end[0]}/{end[1]}/{end[2]}'

		return f'{start_formatted}-{end_formated}'

	def get_meet_day(self, meet_day_int):
		meet_days = ['', 'M', 'T', 'W', 'R', 'F', 'MWF', 'TR']
		return meet_days[meet_day_int]

	def get_hour_minute(self, time):
		return (time.hour, time.minute)

	def get_year_month_day(self, date):
		return (date.year, date.month, date.day)

	def get_section_type(self, section_int):
		section_types = ['', 'Lecture', 'Online']
		return section_types[section_int]

	'''
		Handle the user's choice and redirect
		them to the appropriate view.
		
		@param choice {int} Number corresponding to
		the view in the ordered list menu.
	'''
	def on_choice_selection(self, choice):
		if choice == 1:
			self.go_back()