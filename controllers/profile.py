from .base import BaseController
from views import ProfileView
from models import Student

class ProfileController(BaseController):

	def __init__(self, params, payload):
		super().__init__(params, payload)

		self.__view = ProfileView(self)
		self.__view.render(self.get_profile())

	'''
		Determine which model to use for queries
		based on the "type" key found in
		the payload.

		@return {Model}
	'''
	def get_model(self):
		account_type = self.get_payload()['type']
		if account_type == 'student':
			return Student

	'''
		Queries the database and returns a dictionary
		of values to display in the profile view.

		@return {dict} Values to be displayed
	'''
	def get_profile(self):
		account_id = self.get_payload()['id']
		model = self.get_model()

		try:
			query = (model
				.select()
				.where(getattr(model, 'id') == account_id)
				.get())

			return {
				'id': query.id,
				'username': query.username,
				'first_name': query.first_name,
				'last_name': query.last_name,
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
		if choice == 1:
			self.go_back()
		else:
			self.dispatch('/')


