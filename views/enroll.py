from .base import BaseView

class EnrollView(BaseView):

	def __init__(self, controller):
		super().__init__(controller)

	def render(self, payload):
		self.print_title('Input New Student Info')

		another = 'y'

		while another.lower() == 'y':
			#account
			first_name = self.get_non_empty_string('First Name: ')
			last_name = self.get_non_empty_string('Last Name: ')
			username = self.get_non_empty_string('Username - first initial + last name: ')
			password = self.get_non_empty_string('password - student + \# > 3:')
			#personal
			sex = self.get_int_range('Sex- 1 = M/ 2 = F: ')
			date_of_birth = self.get_non_ get_non_empty_string('Date of Birth - YYYY MM DD: ')
			age = self.get_int_range('Age: ',(18,120))
			#address
			address_street = self.get_non_empty_string('Street address: ')
			address_city = self.get_non_empty_string('City: ')
			address_state = self.get_non_empty_string('State: ')
			address_zip_code = self.get_int_range('Zip 5 digits:', (10000, 99999))
			address_country = self.get_non_empty_string('Country: ')
			#contact
			phone_number = self.get_int_range('Phone number 10 digits:', (1000000000, 9999999999))
			email = self.get_non_empty_string('email: ')

			self.get_controller().

			another = self.get_y_or_n('Add another student? (y/n): ')

		self.get_controller().go_back()
