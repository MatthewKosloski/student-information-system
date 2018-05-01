from .base import BaseView
from table import Table

class ProfileView(BaseView):

	def __init__(self, controller):
		super().__init__(controller)

		self.set_choices([
			'Back'
		])

	'''
		Creates a table from the provided
		payload data.

		@payload {dict}
		@return {Table}
	'''
	def get_profile_table(self, payload):
		table = Table(['FULL NAME', 'STUDENT ID', 'SEX'])
		table.add_row([payload['full_name'], payload['id'], payload['sex']])
		table.add_row(['', '', ''])
		table.add_row(['ADDRESS', 'DATE OF BIRTH', 'AGE'])
		table.add_row([payload['address_street'], payload['date_of_birth'], payload['age']])
		table.add_row([f'{payload["address_city"]}, {payload["address_state"]}', '', ''])
		table.add_row([payload['address_zip_code'], '', ''])
		table.add_row(['', '', ''])
		table.add_row(['PHONE NUMBER', 'EMAIL ADDRESS', ''])
		table.add_row([payload['phone_number'], payload['email'], ''])
			
		return table
		
	def render(self, payload):
		self.print_title('Student Profile')
		
		print(self.get_profile_table(payload))
		print(self.get_choices_list())
		print()

		self.choice_prompt()
