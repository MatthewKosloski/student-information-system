from .base import BaseController
from views import SectionsView
from common_queries import get_term_name
from models import *
from routes import *
import utils

class SectionsController(BaseController):

	def __init__(self, router, payload):
		super().__init__(router, payload)

		self.__view = SectionsView(self)

		route = self.get_route()

		if route == STUDENT_SCHEDULE_TERM_SCHEDULE_ROUTE:
			term_id = self.get_payload()['term_id']
			term = get_term_name(term_id)
			sections = self.process_section_query(self.get_student_schedule())
			self.__view.render({
				'sections': sections,
				'view_title': f'Student schedule for the {term} semester.'
			})
		elif route == SEARCH_RESULTS_ROUTE:
			if 'term_id' in payload:
				term_id = self.get_payload()['term_id']
				term = get_term_name(term_id)
				sections = self.process_section_query(self.get_sections_by_term_id())
				self.__view.render({
					'sections': sections,
					'view_title': f'Sections for the {term} semester.'
				})
			elif 'course_name' in payload:
				sections = self.process_section_query(self.get_sections_by_course_name())
				self.__view.render({
					'sections': sections,
					'view_title': f'Sections for course {self.get_payload()["course_name"]}'
				})

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
				Section.type,
				Term.abbreviation.alias('term'))
			.join(Course, on=(Section.course_id == Course.id))
			.join(Instructor, on=(Section.instructor_id == Instructor.id))
			.join(Term, on=(Section.term_id == Term.id))
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
				Section.type,
				Term.abbreviation.alias('term'))
			.join(Section, on=(Registration.section_id == Section.id))
			.join(Course, on=(Section.course_id == Course.id))
			.join(Term, on=(Section.term_id == Term.id))
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
				Section.type,
				Term.abbreviation.alias('term'))
			.join(Course, on=(Section.course_id == Course.id))
			.join(Term, on=(Section.term_id == Term.id))
			.join(Instructor, on=(Section.instructor_id == Instructor.id))
			.where(Section.term_id == term_id)
			.dicts())

		return query

	'''
		Processes the section query
		before sending it off to the
		appropriate view.

		@param sections {dict}
		@return processed_schedule {list}
	'''
	def process_section_query(self, sections):
		processed_sections = []
		for item in sections:
			processed_sections.append({
				'meet_day': utils.get_meet_day(item['meet_day']),
				'meet_time': utils.concat_start_end_time(
					item['meet_time_start'], item['meet_time_end']),
				'meet_date': utils.concat_start_end_date(
					item['start_date'], item['end_date']),
				'section_type': utils.get_section_type(
					item['type']),
				'course': utils.get_section_str(
					item['name'], item['title'], item['number']),
				'instructor': utils.format_name(
					item['first_name'], item['last_name'], True),
				'meet_location': item['meet_location'],
				'term': item['term']
			})
		return processed_sections

	'''
		Handle the user's choice and redirect
		them to the appropriate view.
		
		@param choice {int} Number corresponding to
		the view in the ordered list menu.
	'''
	def on_choice_selection(self, choice, meta):
		if choice == 1: # Home
			self.go_home()
		elif choice == 2: # Back
			self.go_back()

