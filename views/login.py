from .base import BaseView
import getpass

class LoginView(BaseView):

	def __init__(self, controller):
		super().__init__(controller)
		self.__is_valid_login = False

	def set_login_status(self, status):
		self.__is_valid_login = status
		
	def render(self, payload):
		print()
		print()
		print('Login')
		print()

		while not self.__is_valid_login:

			account = int(input('Account type (1 = Student, 2 = Instructor): '))
			username = input('Username: ')
			password = input('Password: ')
			self.get_controller().login(account, username, password)
