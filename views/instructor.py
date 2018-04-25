from .base import BaseView

class InstructorView(BaseView):

	def __init__(self, controller):
		super().__init__(controller)

		self.set_choices([
			'View Profile',
			'Change Password',
			'Input Grades',
			'View Class Schedule',
			'View Student Grades', 
			'Logout'
		])
		
	def render(self, payload):
		self.print_title('Instructor')
		
		print(self.get_choices_list())
		print()
		print('Instructor view.')
		print()
		self.choice_prompt()