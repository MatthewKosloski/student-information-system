from .base import BaseView
import getpass

class LoginView(BaseView):

	def __init__(self, controller):
		super().__init__(controller)
		self.__is_valid_login = False

	def set_login_status(self, status):
		self.__is_valid_login = status
		
	def render(self, payload):
		self.print_title('Login')

		while not self.__is_valid_login:

			account = self.get_int_range(
				'Account type (1 = Student, 2 = Instructor, 3 = Registrar): ', (1, 3))
			username = self.get_non_empty_string(
				'Username: ', 'Please provide a username.')
			password = self.get_non_empty_string(
				'Password: ', 'Please provide a password.')

			self.get_controller().on_credentials_selection(account, username, password)
