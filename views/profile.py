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
	def get_profile_table(self, profile):
		table = Table(['FULL NAME', 'STUDENT ID', 'SEX'])
		table.add_row([profile['full_name'], profile['id'], profile['sex']])
		table.add_row(['', '', ''])
		table.add_row(['ADDRESS', 'DATE OF BIRTH', 'AGE'])
		table.add_row([profile['address_street'], profile['date_of_birth'], profile['age']])
		table.add_row([f'{profile["address_city"]}, {profile["address_state"]}', '', ''])
		table.add_row([profile['address_zip_code'], '', ''])
		table.add_row(['', '', ''])
		table.add_row(['PHONE NUMBER', 'EMAIL ADDRESS', ''])
		table.add_row([profile['phone_number'], profile['email'], ''])
			
		return table
		
	def render(self, payload):
		self.print_title('Student Profile')
		
		print(self.get_profile_table(payload))
		print(self.get_choices_list())
		print()

		self.choice_prompt()
