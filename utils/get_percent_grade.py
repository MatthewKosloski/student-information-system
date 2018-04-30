'''
	Appends a percent sign
	at the end of the parameter. If
	the parameter is None, return a
	bunch of hyphens.

	@param {float|None} Float to be appended
	with a percent sign
	@return {str} Converted value
'''
def get_percent_grade(float):
	if float != None:
		return str(float) + '%'
	else: 
		return '--.-%'