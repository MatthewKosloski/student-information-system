from .base import BaseController
from views import TermSelectionView
from models import Registration, Term, Section
from account_types import *
from routes import *

class TermSelectionController(BaseController):

	def __init__(self, router, payload):
		super().__init__(router, payload)

		self.__view = TermSelectionView(self)

		route = self.get_route()

		if route == STUDENT_GRADES_SELECT_TERM_ROUTE or \
		route == STUDENT_SCHEDULE_SELECT_TERM_ROUTE:
			self.render_student_terms()
		elif route == INSTRUCTOR_ROSTER_SELECT_TERM_ROUTE:
			self.render_instructor_terms()
		elif route == SEARCH_SELECT_TERM_ROUTE:
			self.render_all_terms()

	'''
		Renders the view with a list of
		the student's registration terms.
	'''
	def render_student_terms(self):
		self.__view.render(self.process_terms(self.get_student_terms()))

	'''
		Renders the view with a list of
		the instructor's terms.
	'''
	def render_instructor_terms(self):
		self.__view.render(self.process_terms(self.get_instructor_terms()))

	'''
		Renders the view with a list of
		all existings terms.
	'''
	def render_all_terms(self):
		self.__view.render(self.process_terms(self.get_all_terms()))

	'''
		Queries the database for the ID and title
		of all the student's registration terms 
		(e.g., 'Fall 2018').

		@return {list}
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

		@return {list}
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

		@return {list}
	'''
	def get_all_terms(self):
		query = (Term
			.select(Term.title, Term.id)
			.dicts())

		return query

	'''
		Separates the registration term titles and
		IDs.

		@param query {dict}
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
		@param meta {Any} The meta value associated
		with the choice.
	'''
	def on_choice_selection(self, choice, meta):
		if choice == 1: # Home
			self.go_home()
		elif choice == 2: # Back
			self.go_back()
		else: # Dynamic choices

			route = self.get_route()
			account_type = self.get_payload()['type']
			account_id = self.get_payload()['id']
			payload = {
				'type': account_type, 
				'id': account_id, 
				'term_id': meta
			}
			
			if route == STUDENT_GRADES_SELECT_TERM_ROUTE or \
			route == STUDENT_SCHEDULE_SELECT_TERM_ROUTE:
				if route == STUDENT_SCHEDULE_SELECT_TERM_ROUTE:
					self.dispatch(STUDENT_SCHEDULE_TERM_SCHEDULE_ROUTE, payload)
				elif route == STUDENT_GRADES_SELECT_TERM_ROUTE:
					self.dispatch(STUDENT_GRADES_TERM_GRADES_ROUTE, payload)
			elif route == INSTRUCTOR_ROSTER_SELECT_TERM_ROUTE:
				self.dispatch(INSTRUCTOR_ROSTER_SELECT_SECTION_ROUTE, payload)
			elif route == SEARCH_SELECT_TERM_ROUTE:
				self.dispatch(SEARCH_RESULTS_ROUTE, payload)

