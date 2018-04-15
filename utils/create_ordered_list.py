'''
	Creates an ordered list of items starting
	at zero.

	Example:

	0. Uno
	1. Dos
	2. Tres

	@param items {list}
	@return output {str}
'''
def create_ordered_list(items):
	output = ''
	for item in items:
		current_index = items.index(item)

		output += str(current_index)
		output += '. '
		output += item
		# Don't append a newline after the last list item
		output += ('' if current_index == (len(items) - 1) else '\n')
	return output