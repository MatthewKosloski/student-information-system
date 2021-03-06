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
		Handle the user's choice and redirect
		them to the appropriate view.
		
		@param choice {int} Number corresponding to
		the view in the ordered list menu.
		@param meta {Any} The meta value associated
		with the choice.
	'''
	def on_choice_selection(self, choice, meta):
		registrar_id = self.get_payload()['id']

		registrar_payload = {'type': REGISTRAR_ACCOUNT_TYPE, 'id': registrar_id}

		if choice == 1: # Change Password
			self.dispatch(CHANGE_PASSWORD_ROUTE, registrar_payload)
		elif choice == 2: # Register Student for Section
			self.dispatch(REGISTRAR_REGISTER_STUDENT_SELECT_ID_ROUTE, registrar_payload)
		elif choice == 3: # Logout
			self.dispatch(HOME_ROUTE)



