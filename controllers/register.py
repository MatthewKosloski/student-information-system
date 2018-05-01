from .base import BaseController
from views import RegisterView
from models import Registration, Section, Course
from peewee import IntegrityError

class RegisterController(BaseController):

	def __init__(self, router, payload):
		super().__init__(router, payload)

		self.__view = RegisterView(self)
		self.__view.render(payload)

	'''
		Gets the section number and course name
		of a section by id.

		@param section_id {int}
		@return {list}
	'''
	def get_name_number(self, section_id):
		try:
			query = (Section
				.select(Section.number, Course.name)
				.join(Course, on=(Section.course_id == Course.id))
				.where(Section.id == section_id)
				.dicts())

			return list(query)[0]
		except IndexError:
			return False

	'''
		Received the section id inputted from user
		along with the student's id.

		@param section_id {str} Primary key of section
		@param student_id {str} Primary key of student
	'''
	def on_id_selection(self, section_id, student_id):
		
		try:
			reg = Registration(section_id=section_id, student_id=student_id)

			if reg.save():
				name_number = self.get_name_number(section_id)
				if name_number:
					self.__view.print_message('Successfully registered for section ' + 
						f'{name_number["number"]} of {name_number["name"]}.')
				else:
					self.__view.print_message('Successfully registered for section.')
			else:
				self.__view.print_message(f'Failed to register for section.')
		except IntegrityError:
			self.__view.print_message('Unable to register for section.')
