from .base import BaseView

class StudentView(BaseView):

	def __init__(self, controller):
		super().__init__(controller)

		self.set_choices([
			'View Profile',
			'Change Password',
			'View Grades',
			# 'View Class Schedule (incomplete)',
			# 'Search for Sections (incomplete)',
			# 'Register for Sections (incomplete)',
			'Logout'
		])
		
	def render(self, payload):
		print()
		print(f'Welcome, {payload["username"]} ({payload["full_name"]})!')
		print()
		print(self.get_choices_list())
		print()
		self.choice_prompt()
