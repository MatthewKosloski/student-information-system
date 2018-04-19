from peewee import *
from views import LoginView
from models import Student
from routes import STUDENT_ROUTE, HOME_ROUTE
from .base import BaseController


class LoginController(BaseController):

	def __init__(self, params, payload):
		super().__init__(params, payload)

		self.__view = LoginView(self)
		self.__view.render(payload)

	'''
		Returns the id, username, and password
		column values in the row with the username.

		@param model {Model} Type of Model to query
		@param username {str} Username of the account
		@return {Model}
	'''
	def get_account(self, model, username):
		try:
			query = (model
				.select(getattr(model, 'id'), 
					getattr(model, 'username'),
					getattr(model, 'password'))
				.where(getattr(model, 'username') == username)
				.get())

			return query
		except DoesNotExist:
			raise ValueError(('Either the username is incorrect' +
				' or the account doesn\'t exist!'))

	'''
		Checks if the user's password in the database
		matches the one provided. If so, they are redirected
		to the student view and the student's ID is passed
		along.

		@param account {int} Type of account selected from view
		@param username {str} Username of the user
		@param password {str} Password to compare to the one in db
	'''
	def login(self, account, username, password):

		if account == 1: # student account
			try:
				db_account = self.get_account(Student, username)

				if db_account.password == password:
					self.__view.set_login_status(True)
					self.dispatch(STUDENT_ROUTE, db_account.id)
				else:
					self.__view.print_message('Incorrect password!')

			except ValueError as e:
				self.__view.print_message(e)
		elif account == 2: # instructor account
			# Not implemented yet. Temporary redirect
			self.dispatch(HOME_ROUTE)


