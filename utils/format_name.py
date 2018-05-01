from .truncate_str import truncate_str

'''
	Concatenates a first name and
	last name. Optionally truncates
	the returned result.

	@param first_name {str}
	@param last_name {str}
	@param is_concatenated {bool}
	@return {str} A truncated Full-name
'''
def format_name(first_name, last_name, is_concatenated = False):
	name = f'{first_name} {last_name}'
	if is_concatenated:
		return truncate_str(name, 25)
	else:
		return name