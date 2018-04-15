from peewee import *
from views import LoginView
from models import Student
from .base import BaseController


class LoginController(BaseController):

	def __init__(self, params):
		super().__init__(params)

		self.__view = LoginView(self)

	def index_action(self, payload):
		self.__view.render()

	def get_account(self, model, username):
		try:
			query = (model
				.select()
				.where(getattr(model, 'username') == username)
				.get())

			return query
		except DoesNotExist:
			raise ValueError(('Either the username is incorrect' +
				' or the account doesn\'t exist!'))

	def login(self, account, username, password):

		if account == 1: # student account
			try:
				db_account = self.get_account(Student, username)

				if db_account.password == password:
					self.__view.set_login_status(True)
					self.dispatch('/student/home', db_account)
				else:
					self.__view.print_message('Incorrect password!')

			except ValueError as e:
				self.__view.print_message(e)
		elif account == 2: # instructor account
			print('Login instructor here')


