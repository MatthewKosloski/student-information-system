from .base import BaseController
from models import Registration, Student
from common_queries import get_term_name, get_section_name
from views import RosterView
import utils

class RosterController(BaseController):

	def __init__(self, router, payload):
		super().__init__(router, payload)

		self.__view = RosterView(self)

		section = get_section_name(payload['section_id'])
		term = get_term_name(payload['term_id'])

		self.__view.render({
			'roster': self.process_section_roster(
			self.get_section_roster()),
			'view_title': f'Class roster for {section} ({term})'
		})

	'''
		Queries the database for students
		belonging to a specific section.
		The student's first name, last name,
		id number, letter grade, and percent
		grade are returned.

		@return query {dict}
	'''
	def get_section_roster(self):
		section_id = self.get_payload()['section_id']
		query = (Registration
			.select(Student.first_name,
				Student.last_name,
				Student.id,
				Registration.letter_grade,
				Registration.percent_grade)
			.join(Student)
			.where(Registration.section_id == section_id)
			.dicts())
		return query

	'''
		Turn the query object into a list.

		@param query {BaseModel}
		@return {list}
	'''
	def process_section_roster(self, query):
		roster = []
		for student in query:
			roster.append({
				'first_name': student['first_name'],
				'last_name': student['last_name'],
				'id': str(student['id']),
				'letter_grade': utils.get_letter_grade(student['letter_grade']),
				'percent_grade': utils.get_percent_grade(student['percent_grade'])
			})
		return roster

	'''
		Handle the user's choice and redirect
		them to the appropriate view.
		
		@param choice {int} Number corresponding to
		the view in the ordered list menu.
		@param meta {Any} The meta value associated
		with the choice.
	'''
	def on_choice_selection(self, choice, meta):
		if choice == 1:
			self.go_back()