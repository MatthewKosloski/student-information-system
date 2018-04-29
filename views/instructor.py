from .base import BaseView

class InstructorView(BaseView):

	def __init__(self, controller):
		super().__init__(controller)

		self.set_choices([
			# 'View Profile',
			'Change Password',
			'Input Grades (incomplete)',
			'Logout'
		])
		
	def render(self, payload):
		self.print_title(f'Welcome, {payload["username"]} ({payload["full_name"]})!')
		
		print(self.get_choices_list())
		print()
		self.choice_prompt()