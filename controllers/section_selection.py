from .base import BaseController
from views import SectionSelectionView
from models import Course, Section
from utils import get_section_str
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
		sections = [get_section_str(section['name'], section['title'], section['number']) 
		for section in query]
		section_ids = [section['id'] for section in query]
		return {
			'sections': sections, 
			'section_ids': section_ids
		}

	'''
		Handle the user's choice and redirect
		them to the appropriate view.
		
		@param choice {int} Number corresponding to
		the view in the ordered list menu.
	'''
	def on_choice_selection(self, choice, meta):
		if choice == 1:
			self.go_home()
		elif choice == 2:
			self.go_back()
		else:
			payload = self.get_payload()
			self.dispatch(INSTRUCTOR_ROSTER_SECTION_ROSTER_ROUTE, {
				'type': payload['type'],
				'id': payload['id'],
				'term_id': payload['term_id'],
				'section_id': meta, 
			})
			