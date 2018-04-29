from .base import BaseController
from views import RegistrarView
from models import Registrar

class RegistrarController(BaseController):

	def __init__(self, params, payload):
		super().__init__(params, payload)

		self.__view = RegistrarView(self)

		self.__view.render(self.get_username_and_full_name(payload))

	'''
		Get the username, firstname, and lastname
		from the registrar.

		@param id {int} ID of the registrar
		@return {dict} A dictionary containing the username
		and full name of the user to be displayed in the
		registrar view.
	'''
	def get_username_and_full_name(self, id):
		try:
			query = (Registrar
				.select(Registrar.username, 
					Registrar.first_name, 
					Registrar.last_name)
				.where(Registrar.id == id)
				.get())

			return {
				'username': query.username,
				'full_name': f'{query.first_name} {query.last_name}'
			}
		except DoesNotExist:
			self.__view.print_message('Account does not exist.')

	'''
		Handle the user's choice and redirect
		them to the appropriate view.
		
		@param choice {int} Number corresponding to
		the view in the ordered list menu.
	'''
	def on_choice_selection(self, choice):
		registrar_id = self.get_payload()
		if choice == 1: # View profile
			# specify type so we can reuse profile module
			self.dispatch('/registrar/profile', {'type': 'registrar', 'id': registrar_id})
		elif choice == 2: # view courses
		# specify type so we can reuse password module
			self.dispatch('/change-password', {'type': 'student', 'id': registrar_id})
		elif choice == 3:
			self.dispatch('/student/grades', registrar_id)
		elif choice == 4: # Logout
			self.dispatch('/')