from .base import BaseView

class ScheduleView(BaseView):

	def __init__(self, controller):
		super().__init__(controller)

		self.set_choices([
			'Back'
		])
		
	def render(self, payload):
		self.print_title('Schedule view')
		
		print(self.get_choices_list())
		print()
		print('This is the schedule view')
		print()
		self.choice_prompt()