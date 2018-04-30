from .truncate_str import truncate_str

'''
	Formats and truncates the section and 
	zero-pads the section number.

	@param name {str}
	@param title {str}
	@param number {str}
	@return {str}
'''
def get_section_str(name, title, number):
	if number < 10:
		number = f'0{number}'

	course = f'{name}-{number} {title}'
	return truncate_str(course, 25)