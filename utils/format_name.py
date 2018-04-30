from .truncate_str import truncate_str

'''
	Formats and truncates a name.

	@param first_name {str}
	@param last_name {str}
	@return {str} A truncated Full-name
'''
def format_name(first_name, last_name):
	instructor = f'{first_name} {last_name}'
	return truncate_str(instructor, 25)