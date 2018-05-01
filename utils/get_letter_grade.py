'''
	Maps an integer to a letter grade and
	returns a hyphen if the parameter is
	None.

	@param integer {int|None} Integer to be converted
	to a letter
	@return {str} Converted value  
'''
def get_letter_grade(integer):
	if integer != None:
		letters = ['A', 'B', 'C', 'D', 'F']
		return letters[integer - 1]
	else: 
		return '-'