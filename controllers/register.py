from .base import BaseController
from views import RegisterView
from models import Registration, Student
from common_queries import get_section_name, get_username_and_full_name
from peewee import IntegrityError
from routes import *

class RegisterController(BaseController):

	def __init__(self, router, payload):
		super().__init__(router, payload)

		self.__view = RegisterView(self)

		route = self.get_route()

		if route == STUDENT_REGISTER_ROUTE:
			self.__student_id = self.get_payload()['id']
		elif route == REGISTRAR_REGISTER_STUDENT_ROUTE:
			self.__student_id = self.get_payload()['student_id']

		self.__student_name = get_username_and_full_name(
			Student, self.__student_id)['full_name']

		self.__view.render({
			'view_title': f'Register {self.__student_name} for Sections'
		})

	'''
		Received the section id inputted from user
		along with the student's id.

		@param section_id {str} Primary key of section
	'''
	def on_id_selection(self, section_id):

		try:
			reg = Registration(
				section_id=section_id, 
				student_id=self.__student_id)

			if reg.save():

				section_name = get_section_name(section_id)
	
				if section_name:
					self.__view.print_message(
						f'Successfully registered {self.__student_name} for {section_name}.')
				else:
					self.__view.print_message('Successfully registered for section.')
			else:
				self.__view.print_message(f'Failed to register for section.')
		except IntegrityError:
			self.__view.print_message('Unable to register for section.')
