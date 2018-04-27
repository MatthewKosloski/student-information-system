class Table:

	def __init__(self, columns, padding=5):

		self.__columns = columns
		self.__rows = []
		self.__padding = 5

	'''
		Adds a row to the table.

		@param fields {tuple} Arguments passed to
		the method, which are packed into a tuple.
	'''
	def add_row(self, fields):
		self.__rows.append(fields)

	'''
		Takes a row and returns a formatted string of it.

		@param row {tuple}
		@return 
	'''
	def row_str(self, row):
		output = ''
		for index, field in enumerate(row):
			field_len = len(field)
			longest_column_len = self.get_longest_column_field_len(index)
			multiple = (longest_column_len - field_len)
			width = ' ' * (multiple + self.__padding)
			output += field + width
		output += '\n'
		return output

	'''
		Returns the fields in the rows
		associated with the column.

		@param column {int}
		@return fields {list}
	'''
	def get_column_fields(self, column):
		fields = []
		for row in self.__rows:
			fields.append(row[column])
		return fields

	'''
		Returns the length of the longest
		field in a column (including the title
		of the column itself).

		@param column {int} Index of column
		@return {int} Length of longest field in column
	'''
	def get_longest_column_field_len(self, column):
		column_len = len(self.__columns[column])
		fields = self.get_column_fields(column)
		longest_column_field_len = len(max(fields, key=len))
		return max(column_len, longest_column_field_len)

	def __str__(self):
		output = self.row_str(self.__columns) + '\n'
		output += '\n'
		for row in self.__rows:
			output += self.row_str(row) + '\n'
		return output
