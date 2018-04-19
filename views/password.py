from .base import BaseView
import getpass

class PasswordView(BaseView):

	def __init__(self, controller):
		super().__init__(controller)
		self.__password_has_changed = False

	def set_password_status(self, status):
		self.__password_has_changed = status
		
	def render(self, payload):
		self.print_title('Change Password')

		while not self.__password_has_changed:

			old = print('Old Password: ')
			new = print('New Password: ')
			new_confirmed = print('Confirm New Password: ')

			self.get_controller().change_password(old, new, new_confirmed)
