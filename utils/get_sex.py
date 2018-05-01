'''
	Maps an integer to a
	sex string.

	@param sex_int {int} 1 or 2
	@return sexes {str} Male or Female
'''
def get_sex(sex_int):
	sexes = ['Male', 'Female']
	return sexes[sex_int - 1]