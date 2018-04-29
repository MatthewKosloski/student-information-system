from .base import BaseController
from views import InputGradesView
from models import Section, Registration

class InputGradesController(BaseController):

	def __init__(self, router, payload):
		super().__init__(router, payload)

		self.__view = InputGradesView(self)
		self.__view.render(payload)
	
	def on_details_selection(self, section_id, student_id, percent_grade):
		instructor_id = self.get_payload()['id']

		if self.instructor_has_section(instructor_id, section_id):
			letter_grade = self.get_letter_grade_int(percent_grade)
			has_updated = self.input_grade(student_id, section_id, percent_grade, letter_grade)
			if has_updated:
				self.__view.print_message(f'Student #{student_id} in section #{section_id} now ' + 
					f'has grade {self.get_letter_grade(letter_grade)} ({self.format_percent(percent_grade)}).')
			else:
				self.__view.print_message('No grades have been updated.')
		else:
			print('Could not input grade. Either you or the student are not associated with the section.')

	'''
		Checks to make sure the instructor
		teaches the section.

		@param instructor_id {int}
		@param section_id {int}
		@return {bool}
	'''
	def instructor_has_section(self, instructor_id, section_id):
		query = (Section
			.select()
			.where(Section.id == section_id,
				Section.instructor_id == instructor_id)
			.exists())

		return query

	'''
		Inputs the letter grade and percent grade into a
		row in the Registration table.

		@param student_id {int}
		@param section_id {int}
		@param percent_grade {float}
		@param letter_grade {int}
	'''
	def input_grade(self, student_id, section_id, percent_grade, letter_grade):
		update = (Registration
			.update(percent_grade=percent_grade,
				letter_grade=letter_grade)
			.where(Registration.student_id == student_id,
				Registration.section_id == section_id))

		return update.execute()

	'''
		Converts the letter grade int
		to a letter grade.

		@param letter_grade_int {int}
		@return {str}
	'''
	def get_letter_grade(self, letter_grade_int):
		grades = ['A', 'B', 'C', 'D', 'F']
		return grades[letter_grade_int - 1]

	'''
		Maps a percent to an integer
		representing a letter grade (1 = A,
		2 = B ... 5 = F).

		@param percent_grade {float}
		@return {int}
	'''
	def get_letter_grade_int(self, percent_grade):
		if percent_grade >= 90:
			return 1
		elif percent_grade >= 80 and percent_grade <= 89:
			return 2
		elif percent_grade >= 70 and percent_grade <= 79:
			return 3
		elif percent_grade >= 60 and percent_grade <= 69:
			return 4
		else:
			return 5

	def format_percent(self, percent_grade):
		return '{:.2f}%'.format(percent_grade)



