from .base import BaseController
from views import LoginView
from models import Student, Instructor
from routes import *

class LoginController(BaseController):

	def __init__(self, router, payload):
		super().__init__(router, payload)

		self.__view = LoginView(self)
		self.__view.render(payload)

	'''
		Determines which type of login to do
		based on the account selection.

		@param account {int}
		@param username {str}
		@param password {str}
	'''
	def on_credentials_selection(self, account, username, password):

		if account == 1:
			self.login(Student, STUDENT_ROUTE, username, password)
		elif account == 2:
			self.login(Instructor, INSTRUCTOR_ROUTE, username, password)

	'''
		Checks if the user's password in the database
		matches the one provided. If so, they are redirected
		to the provided route and the account's ID is passed
		along.

		@param model {BaseModel} Type of model to query
		@param route {str} Where to take user on successful login
		@param username {str}
		@param password {str}
	'''
	def login(self, model, route, username, password):
		try:
			db_account = self.get_account(model, username)

			if db_account.password == password:
				self.__view.set_login_status(True)
				self.dispatch(route, {'id': db_account.id})
			else:
				self.__view.print_message('Incorrect password!')

		except ValueError as e:
			self.__view.print_message(e)

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



