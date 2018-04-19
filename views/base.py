from utils import create_ordered_list

class BaseView():

	def __init__(self, controller):
		self.__controller = controller
		self.__choices = ['Exit']

	'''
		Get the controller for this view.

		@return {cls}
	'''
	def get_controller(self):
		return self.__controller

	'''
		Get the choices

		@return {list}
	'''
	def get_choices(self):
		return self.__choices

	'''
		Set the choices.

		@param choices {list}
	'''
	def set_choices(self, choices):
		self.__choices += choices

	'''
		Print the title and optional subtitle
		to the view.

		@param title {str}
		@param subtitle {str}
	'''
	def print_title(self, title, subtitle = None):
		print()
		print()
		print(title)
		print()
		if subtitle:
			print(subtitle)
			print()

	'''
		Returns an ordered list of the choices.

		@return {str}
	'''
	def get_choices_list(self):
		return create_ordered_list(self.__choices)

	'''
		Handle the choice provided by
		the user and send it to the
		controller.

		@param choice {int}
	'''
	def handle_choice(self, choice):
		if choice != 0:
			self.__controller.on_choice_selection(int(choice))

	'''
		Asks the user for a valid integer
		that corresponds to the index of an
		item in self.__choices.

		@param on_choice {func}
	'''
	def choice_prompt(self):
		choice = -1
		minimum = 0
		maximum = len(self.__choices) - 1

		while not (choice >= minimum and choice <= maximum):
			try:
				choice = int(input('> '))
			except ValueError as e:
				print(f'Please enter an integer between {minimum} and {maximum}.')

		self.handle_choice(choice)

	'''
		Prints a message to the view. Use for
		error handling, etc.

		@param message {str}
	'''
	def print_message(self, message):
		print(message)


