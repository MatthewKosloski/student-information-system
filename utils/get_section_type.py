'''
	Maps an integer to a section type.

	@param section_int {int}
	@return {str}
'''
def get_section_type(section_int):
	section_types = ['', 'Lecture', 'Online']
	return section_types[section_int]