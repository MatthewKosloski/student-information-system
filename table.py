class Table:

	def __init__(self):

		self.__columns = []
		self.__rows = []

	def add_columns(self, columns):
		self.__columns += columns

	def add_row(self, *fields):
		self.__rows.append(fields)

	def get_rows(self):
		return self.__rows

	def get_columns(self):
		return self.__columns

	def get_longest_field_len(self):
		longest = 0
		for row in self.__rows:
			longest_row = len(max(row))
			if longest_row > longest:
			 longest = longest_row
		return longest

	def get_longest_column_len(self):
		return len(max(self.__columns))

	def get_longest(self):

		longest_field = self.get_longest_field_len()
		longest_column = self.get_longest_column_len()

		return max([longest_field, longest_column])

	def row_str(self, row):
		formatted_str = ('{:<{width}} ' * (len(row) - 1)).format(width=self.get_longest())
		return formatted_str.format(*row)

	def print_columns(self):
		output = ''
		for column in self.__columns:
			output += '{:<{self}} {:<30}'.format('Full Name', 'Email Address')

	def __str__(self):
		output = ''
		for column in self.__columns:
			output += column + ' '
		output += '\n'
		for row in self.__rows:
			output += self.row_str(row) + '\n'
		return output
