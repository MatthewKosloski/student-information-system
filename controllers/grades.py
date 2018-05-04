from .base import BaseController
from utils import get_letter_grade, get_percent_grade
from common_queries import get_term_name
from views import GradesView
from models import *

class GradesController(BaseController):

	def __init__(self, router, payload):
		super().__init__(router, payload)

		self.__view = GradesView(self)
		
		term_name = get_term_name(payload['term_id'])
		grades = self.process_get_student_grades(self.get_student_grades())

		self.__view.render({
			'grades': grades,
			'view_title': f'{term_name} Semester Grades'
		})

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
				'grade': get_letter_grade(item['letter_grade']),
				'percent': get_percent_grade(item['percent_grade'])
			})
		return simplified_grades

	'''
		Handle the user's choice and redirect
		them to the appropriate view.
		
		@param choice {int} Number corresponding to
		the view in the ordered list menu.
		@param meta {Any} The meta value associated
		with the choice.
	'''
	def on_choice_selection(self, choice, meta):
		student_id = self.get_payload()
		if choice == 1:
			self.go_back()
