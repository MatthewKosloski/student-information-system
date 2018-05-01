from .base import BaseController
from views import RegistrarView
from models import Registrar
from common_queries import get_username_and_full_name
from account_types import REGISTRAR_ACCOUNT_TYPE
from routes import *

class RegistrarController(BaseController):

	def __init__(self, router, payload):
		super().__init__(router, payload)

		self.__view = RegistrarView(self)

		try:
			self.__view.render(get_username_and_full_name(Registrar, payload['id']))
		except ValueError as e:
			self.__view.print_message(e)
	'''
		Get the username, firstname, and lastname
		from the registrar.

		@param id {int} ID of the registrar
		@return {dict} A dictionary containing the username
		and full name of the user to be displayed in the
		registrar view.
		Handle the user's choice and redirect
		them to the appropriate view.
		
		@param choice {int} Number corresponding to
		the view in the ordered list menu.
	'''
	def on_choice_selection(self, choice):
		registrar_id = self.get_payload()
		if choice == 1: # Change Password
			# specify type so we can reuse profile module
			self.dispatch(CHANGE_PASSWORD_ROUTE, registrar_payload)
		elif choice == 2: # Enroll Student
			#pecify type so we can reuse password module
			self.dispatch()
		elif choice == 3: # Drop Student
			self.dispatch(SEARCH_ROUTE, registrar_payload)
		elif choice == 4: # Logout
			self.dispatch('HOME_ROUTE')