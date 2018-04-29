from .base import BaseController
from views import GradesView
from models import *


class GradesController(BaseController):

	def __init__(self, router, payload):
		super().__init__(router, payload)

		self.__view = GradesView(self)
		self.__view.render({
			'grades': self.process_get_student_grades(self.get_student_grades()),
			'view_title': f'Student grades for the {self.get_term_name()} semester.'
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

		return self.process_get_term_name(query)

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
		Returns the student's letter grade and percent grade
		for a section along with the course's title and name. 
		
		@return {list} Letter grade and percent grade from a row
		in the registration table along with course title and name
		from the course table.
	'''
	def get_student_grades(self):
		student_id = self.get_payload()['id']
		term_id = self.get_payload()['term_id']
		query = (Registration
			.select(Registration.letter_grade,
				Registration.percent_grade, 
				Course.name, 
				Course.title)
			.join(Section, on=(Registration.section_id == Section.id))
			.join(Course, on=(Section.course_id == Course.id))
			.where(Registration.student_id == student_id, 
				Section.term_id == term_id)
			.dicts())

		return query

	'''
		Modifies the results returned by the
		database by combining the course name
		and title, getting the letter corresponding
		to the letter_grade integer, and appending
		a percent sign at the end of the percent.

		@param grades {list} DB results
		@return simplified_grades {list} Altered list 
	'''
	def process_get_student_grades(self, grades):
		simplified_grades = []
		for item in grades:
			simplified_grades.append({
				'course': f'{item["name"]} {item["title"]}',
				'grade': self.get_letter_grade(item['letter_grade']),
				'percent': self.get_percent_grade(item['percent_grade'])
			})
		return simplified_grades


	'''
		Maps an integer to a letter grade and
		returns a hyphen if the parameter is
		None.

		@param {int|None} Integer to be converted
		to a letter
		@return {str} Converted value  
	'''
	def get_letter_grade(self, integer):
		if integer != None:
			letters = ['A', 'B', 'C', 'D', 'F']
			return letters[integer - 1]
		else: 
			return '-'

	'''
		Appends a percent sign
		at the end of the parameter. If
		the parameter is None, return a
		bunch of hyphens.

		@param {float|None} Float to be appended
		with a percent sign
		@return {str} Converted value
	'''
	def get_percent_grade(self, float):
		if float != None:
			return str(float) + '%'
		else: 
			return '--.-%'

	'''
		Handle the user's choice and redirect
		them to the appropriate view.
		
		@param choice {int} Number corresponding to
		the view in the ordered list menu.
	'''
	def on_choice_selection(self, choice, meta):
		student_id = self.get_payload()
		if choice == 1:
			self.go_back()


