'''
	Truncates a string if the
	length of the string is greater
	than the provided length integer.

	@param str {str}
	@param to_length {int}
	@return {str}
'''
def truncate_str(str, to_length):
	return (str[:to_length] + '...') if len(str) > to_length else str