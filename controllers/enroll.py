from .base import BaseController
from views import EnrollView
from utils import to_mm_dd_yyyy, format_phone_number
from models import *

class EnrollController(BaseController):

	def __init__(self, router, payload):
		super().__init__(router, payload)

		self.__view = EnrollView(self)
		self.__view.render(payload)

	'''
	'''
	def on_details_selection(self, section_id, student_id, percent_grade):
		instructor_id = self.get_payload()['id']

		if self.instructor_has_section(instructor_id, section_id):
			letter_grade = utils.get_letter_grade_int(percent_grade)

			has_updated = self.input_grade(
				student_id, 
				section_id, 
				percent_grade, 
				letter_grade)

			if has_updated:
				self.__view.print_message(f'Student #{student_id} in section #{section_id} now ' + 
					f'has grade {utils.get_letter_grade(letter_grade)} ({utils.format_percent(percent_grade)}).')
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
