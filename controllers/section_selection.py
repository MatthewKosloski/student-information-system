from .base import BaseController
from views import SectionSelectionView
from models import Course, Section
from routes import *

class SectionSelectionController(BaseController):

	def __init__(self, router, payload):
		super().__init__(router, payload)

		self.__view = SectionSelectionView(self)
		self.__view.render(self.process_instructor_sections(
			self.get_instructor_term_sections()))

	'''
		Get the course name, course title, section
		number, and section id of all the instructor's 
		sections from a specific term.

		@return {dict}
	'''
	def get_instructor_term_sections(self):
		instructor_id = self.get_payload()['id']
		term_id = self.get_payload()['term_id']

		query = (Section
			.select(
				Course.name, 
				Course.title, 
				Section.number,
				Section.id)
			.join(Course, on=(Section.course_id == Course.id))
			.where(Section.instructor_id == instructor_id, 
				Section.term_id == term_id)
			.dicts())
		
		return query

	'''
		Separates the section strings and IDs into
		two different lists.

		@param query {unknown}
		@return {dict}
	'''
	def process_instructor_sections(self, query):
		sections = [self.get_section_str(section) for section in query]
		section_ids = [section['id'] for section in query]
		return {
			'sections': sections, 
			'section_ids': section_ids
		}

	'''
		Returns a formatted string that concatenates 
		the course title and section number to the 
		course name. (e.g., CPSC-3310-01 Intro to 
		Object-oriented Programming)

		@param section {dict}
		@return {str}
	'''
	def get_section_str(self, section):
		name = section['name']
		number = section['number']
		title = section['title']

		return f'{name}-{number} {title}'

	'''
		Handle the user's choice and redirect
		them to the appropriate view.
		
		@param choice {int} Number corresponding to
		the view in the ordered list menu.
	'''
	def on_choice_selection(self, choice, meta):
		if choice == 1:
			self.go_back()
		else:
			self.dispatch(INSTRUCTOR_ROSTER_SECTION_ROSTER_ROUTE, 
				{'section_id': meta})
			