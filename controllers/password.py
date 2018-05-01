from .base import BaseController
from views import PasswordView
from models import Student, Instructor
from account_types import *

class PasswordController(BaseController):

	def __init__(self, router, payload):
		super().__init__(router, payload)

		self.__view = PasswordView(self)
		self.__view.render(payload)

	'''
		Determine which model to use for queries
		based on the "type" key found in
		the payload.

		@return {Model}
	'''
	def get_model(self):
		account_type = self.get_payload()['type']
		if account_type == STUDENT_ACCOUNT_TYPE:
			return Student
		elif account_type == INSTRUCTOR_ACCOUNT_TYPE:
			return Instructor

	'''
		Gets the user's current password from the
		database. Query is based on the user's id,
		which is provided in the payload.

		@return {str} User's current password
	'''
	def get_password(self):
		account_id = self.get_payload()['id']
		model = self.get_model()

		try:
			query = (model
				.select(getattr(model, 'password'))
				.where(getattr(model, 'id') == account_id)
				.get())

			return query.password
		except DoesNotExist:
			raise ValueError('Account does not exist.')

	'''
		Changes the user's password to the provided
		password parameter.

		@param password {str} New password
		@return updated_rows {int} Amount of rows updated
	'''
	def set_password(self, password):
		account_id = self.get_payload()['id']
		model = self.get_model()

		updated_rows = (model
			.update({getattr(model, 'password'): password})
			.where(getattr(model, 'id') == account_id)
			.execute())
		return updated_rows

	'''
		Take input from the view and try to update
		the user's password. Checks if the user entered
		the new password correct two times. Checks if
		the user's old password is the same as the
		one in the database.

		@param old {str} User's old password
		@param new {str} User's desired new password
		@param new_confirmed {str} User's desired 
		password (again)
	'''
	def change_password(self, old, new, new_confirmed):
		if new == new_confirmed:
			current_db_password = self.get_password()
			if old == current_db_password:
				updated_rows = self.set_password(new)
				if updated_rows == 1:
					self.__view.print_message('Password has been changed.')
				else:
					self.__view.print_message('Password has NOT been changed.')
				self.__view.set_password_status(True)
				self.go_back()
			else:
				self.__view.print_message('Old password does not ' + 
					'match what is on record.')
		else:
			self.__view.print_message('Confirmed password does not ' + 
				'match the new password.')
