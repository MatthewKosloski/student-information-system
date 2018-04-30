from .base import BaseController
from views import TermSelectionView
from models import Registration, Term, Section
from routes import *

class TermSelectionController(BaseController):

	def __init__(self, router, payload):
		super().__init__(router, payload)

		self.__view = TermSelectionView(self)

		if self.get_route() == STUDENT_GRADES_SELECT_TERM_ROUTE or \
		self.get_route() == STUDENT_SCHEDULE_SELECT_TERM_ROUTE:
			self.render_student_terms()
		elif self.get_route() == INSTRUCTOR_ROSTER_SELECT_TERM_ROUTE:
			self.render_instructor_terms()
		elif self.get_route() == SEARCH_SELECT_TERM_ROUTE:
			self.render_all_terms()

	def render_student_terms(self):
		self.__view.render(self.process_terms(self.get_student_terms()))

	def render_instructor_terms(self):
		self.__view.render(self.process_terms(self.get_instructor_terms()))

	def render_all_terms(self):
		self.__view.render(self.process_terms(self.get_all_terms()))

	'''
		Queries the database for the ID and title
		of all the student's registration terms 
		(e.g., 'Fall 2018')

		@return {dict}
	'''
	def get_student_terms(self):
		student_id = self.get_payload()['id']
		query = (Registration
			.select(Term.title, Term.id)
			.distinct()
			.join(Section, on=(Registration.section_id == Section.id))
			.join(Term, on=(Section.term_id == Term.id))
			.where(Registration.student_id == student_id)
			.dicts())

		return query

	'''
		Queries the database for the ID and title
		of all the instructor's terms (e.g., 'Fall 2018').

		@return {dict}
	'''
	def get_instructor_terms(self):
		instructor_id = self.get_payload()['id']
		query = (Section
			.select(Term.title, Term.id)
			.distinct()
			.join(Term, on=(Section.term_id == Term.id))
			.where(Section.instructor_id == instructor_id)
			.dicts())

		return query

	'''
		Queries the database for all terms,
		returning title and ID columns.

		@return {dict}
	'''
	def get_all_terms(self):
		query = (Term
			.select(Term.title, Term.id)
			.dicts())

		return query

	'''
		Separates the registration term titles and
		IDs.

		@param query {unknown}
		@return payload {dict}
	'''
	def process_terms(self, query):
		terms = [term['title'] for term in query]
		term_ids = [term['id'] for term in query]
		return {
			'terms': terms, 
			'term_ids': term_ids
		}

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
			route = self.get_route()

			if route == STUDENT_GRADES_SELECT_TERM_ROUTE or \
			route == STUDENT_SCHEDULE_SELECT_TERM_ROUTE:
				student_id = self.get_payload()['id']
				student_payload = {'type': 'student', 'id': student_id, 'term_id': meta}
				if route == STUDENT_SCHEDULE_SELECT_TERM_ROUTE:
					self.dispatch(STUDENT_SCHEDULE_TERM_SCHEDULE_ROUTE, student_payload)
				elif route == STUDENT_GRADES_SELECT_TERM_ROUTE:
					self.dispatch(STUDENT_GRADES_TERM_GRADES_ROUTE, student_payload)
			elif route == INSTRUCTOR_ROSTER_SELECT_TERM_ROUTE:
				instructor_id = self.get_payload()['id']
				instructor_payload = {'id': instructor_id, 'term_id': meta}
				self.dispatch(INSTRUCTOR_ROSTER_SELECT_SECTION_ROUTE, instructor_payload)
			elif route == SEARCH_SELECT_TERM_ROUTE:
				self.dispatch(SEARCH_RESULTS_ROUTE, {'term_id': meta})

