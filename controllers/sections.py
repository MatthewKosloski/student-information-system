from .base import BaseController
from views import SectionsView
from utils import *
from models import *

class SectionsController(BaseController):

	def __init__(self, router, payload):
		super().__init__(router, payload)

		self.__view = SectionsView(self)

		if self.get_route_parts()[0] == 'student':
			term = self.process_get_term_name(self.get_term_name()) 
			sections = self.process_section_query(self.get_student_schedule())
			self.__view.render({
				'sections': sections,
				'view_title': f'Student schedule for the {term} semester.'
			})
		elif self.get_route_parts()[0] == 'search':
			if 'term_id' in payload:
				term = self.process_get_term_name(self.get_term_name()) 
				sections = self.process_section_query(self.get_sections_by_term_id())
				self.__view.render({
					'sections': sections,
					'view_title': f'Sections for the {term} semester.'
				})
			elif 'course_name' in payload:
				sections = self.process_section_query(self.get_sections_by_course_name())
				self.__view.render({
					'sections': sections,
					'view_title': f'Sections for course {self.get_payload()["course_name"]}.'
				})

	'''
		Queries the database for the title
		column in terms with a specific ID.

		@return {str}
	'''
	def get_term_name(self):
		term_id = self.get_payload()['term_id']
		query = (Term
			.select(Term.title)
			.where(Term.id == term_id)
			.dicts())

		return query

	'''
		Processes the get_term_name query by
		returning the first result.

		@param query
		@return {str}
	'''
	def process_get_term_name(self, query):
		term_name = []
		for item in query:
			term_name.append(item['title'])
		return term_name[0]

	'''
		Queries the database for sections
		with a specific course name. This is 
		used for searching for sections by course
		name.

		@return {list}
	'''
	def get_sections_by_course_name(self):
		course_name = self.get_payload()['course_name']
		query = (Section
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
			.join(Course, on=(Section.course_id == Course.id))
			.join(Instructor, on=(Section.instructor_id == Instructor.id))
			.where(Course.name == course_name)
			.dicts())

		return query

	'''
		Queries the database and returns
		a student's schedule from a specific
		term.

		@return {list}
	'''
	def get_student_schedule(self):
		student_id = self.get_payload()['id']
		term_id = self.get_payload()['term_id']
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
			.where(Registration.student_id == student_id, 
				Section.term_id == term_id)
			.dicts())

		return query

	'''
		Queries the database for sections
		from a term (e.g., Fall 2018). This
		is used for searching for sections
		by term.
	'''
	def get_sections_by_term_id(self):
		term_id = self.get_payload()['term_id']
		query = (Section
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
			.join(Course, on=(Section.course_id == Course.id))
			.join(Instructor, on=(Section.instructor_id == Instructor.id))
			.where(Section.term_id == term_id)
			.dicts())

		return query

	'''
		Refines the student schedule results from
		the database.

		@param schedule {dict}
		@return processed_schedule {list}
	'''
	def process_section_query(self, schedule):
		processed_schedule = []
		for item in schedule:
			processed_schedule.append({
				'meet_day': self.format_meet_day(item['meet_day']),
				'meet_time': self.format_meet_time(item['meet_time_start'], item['meet_time_end']),
				'meet_date': self.format_meet_date(item['start_date'], item['end_date']),
				'section_type': self.format_section_type(item['type']),
				'course': self.format_course(item['name'], item['title'], item['number']),
				'instructor': self.format_instructor(item['first_name'], item['last_name']),
				'meet_location': item['meet_location']
			})
		return processed_schedule

	'''
		Formats and truncates the course and 
		zero-pads the section number.

		@param name {str}
		@param title {str}
		@param number {str}
		@return {str}
	'''
	def format_course(self, name, title, number):
		if number < 10:
			number = f'0{number}'

		course = f'{name}-{number} {title}'
		return truncate_str(course, 25)

	'''
		Formats and truncates the instructor.

		@param first_name {str}
		@param last_name {str}
		@return {str}
	'''
	def format_instructor(self, first_name, last_name):
		instructor = f'{first_name} {last_name}'
		return truncate_str(instructor, 25)

	'''
		Concatenates and truncates the starting
		and ending meet times.

		@param meet_time_start {time}
		@param meet_time_end {time}
		@param {str}
	'''
	def format_meet_time(self, meet_time_start, meet_time_end):
		start_formatted = to_hh_mm(meet_time_start)
		end_formatted = to_hh_mm(meet_time_end)

		meet_time = f'{start_formatted} to {end_formatted}'
		return truncate_str(meet_time, 25)

	'''
		Concatenates and truncates the starting
		and ending meet dates.

		@param start_date {date}
		@param end_date {date}
		@param {str}
	'''
	def format_meet_date(self, start_date, end_date):
		start_formatted = to_mm_dd_yyyy(start_date)
		end_formatted = to_mm_dd_yyyy(end_date)

		meet_date = f'{start_formatted} to {end_formatted}'
		return truncate_str(meet_date, 25)

	'''
		Maps an integer to a day of the week.

		@param meet_day_int {int}
		@return {str}
	'''
	def format_meet_day(self, meet_day_int):
		meet_days = ['', 'M', 'T', 'W', 'R', 'F', 'MWF', 'TR']
		return meet_days[meet_day_int]

	'''
		Maps an integer to a section type.

		@param section_int {int}
		@return {str}
	'''
	def format_section_type(self, section_int):
		section_types = ['', 'Lecture', 'Online']
		return section_types[section_int]

	'''
		Handle the user's choice and redirect
		them to the appropriate view.
		
		@param choice {int} Number corresponding to
		the view in the ordered list menu.
	'''
	def on_choice_selection(self, choice, meta):
		if choice == 1:
			self.go_back()





