from utils import create_ordered_list

class BaseView():

	def __init__(self, controller):
		self.__controller = controller
		self.__choices = ['Exit']
		self.__choices_meta = ['']

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
	def set_choices(self, choices, choices_meta = []):
		self.__choices += choices

		# Each choice has empty string meta value
		# if no argument is provided.
		if len(choices_meta) == 0:
			self.__choices_meta += ['' for choice in choices]
		else:
			self.__choices_meta += choices_meta

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
			self.__controller.on_choice_selection(int(choice), self.__choices_meta[choice])

	'''
		Keeps prompting the user for
		a string if no string is provided.

		@param input_str {str} Text to be prompted to user
		@param err_str {str} Text printed if no string is provided
		@return val {str} String received from user
	'''
	def get_non_empty_string(self, input_str, err_str):
		while True:
			val = input(input_str)

			if not val:
				print(err_str)
				continue
			else:
				break
		return val

	'''
		Asks the user for a "Y" or "N."

		@param input_str {str} Text to be prompted to user
		@return val {str} String received from user
	'''
	def get_y_or_n(self, input_str):
		while True:
			val = input(input_str)

			if val.lower() == 'y' or val.lower() == 'n':
				break
			else:
				print('Please enter either "y" or "n."')
				continue
			
		return val

	'''
		Asks the user for an integer.

		@param input_str {str} Text to be prompted to user
		@param err_str {str} Text to display when not integer
		@return val {int}
	'''
	def get_int(self, input_str, err_str):
		while True:
			try:
				val = int(input(input_str))
			except ValueError:
				print(err_str)
				continue
			else:
				break
		return val

	'''
		Keeps prompting the user to
		enter an integer between a given range.

		@param input_str {str} Text to be prompted to user
		@param range {tuple} Tuple of two integers, where the
		first is the min and second is the max e.g., (1, 2)
		@return val {int} Int received from user
	'''
	def get_int_range(self, input_str, range):
		# init val to the integer less than the min
		val = range[0] - 1

		while not (val >= range[0] and val <= range[1]):
			try:
				val = int(input(input_str))
			except ValueError as e:
				print(f'Please enter an integer between {range[0]} and {range[1]}.')
		return val

	'''
		Keeps prompting the user to
		enter a float between a given range.

		@param input_str {str} Text to be prompted to user
		@param range {tuple} Tuple of two floats, where the
		first is the min and second is the max e.g., (0.0, 100.0)
		@return val {float} Float received from user
	'''
	def get_float_range(self, input_str, range):
		# init val to the integer less than the min
		val = range[0] - 1

		while not (val >= range[0] and val <= range[1]):
			try:
				val = float(input(input_str))
			except ValueError as e:
				print(f'Please enter a float between {range[0]} and {range[1]}.')
		return val

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

		choice = self.get_int_range('> ', (minimum, maximum))
		self.handle_choice(choice)

	'''
		Prints a message to the view. Use for
		error handling, etc.

		@param message {str}
	'''
	def print_message(self, message):
		print(message)

	'''
		Returns a friendly greeting string.

		@param username {str}
		@param full_name {str}
		@return {str}
	'''
	def get_greeting(self, username, full_name):
		return f'Welcome, {username} ({full_name})!'


