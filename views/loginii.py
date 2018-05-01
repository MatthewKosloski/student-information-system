from .base import BaseView
import getpass

class LoginiiView(BaseView):

	def __init__(self, controller):
		super().__init__(controller)
		self.__is_valid_login = False

	def set_login_status(self, status):
		self.__is_valid_login = status
		
	def render(self, payload):
		print()
		print()
		print('Choose student to view')
		print()

		while not self.__is_valid_login:

			account = 1
			username = input('Username: ')
			self.get_controller().login(account, username,)
