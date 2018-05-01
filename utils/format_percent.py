'''
	Takes an integer or floating point
	number and returns a percentage with
	.2 precision.

	@param num {int|float}
	@return {str}
'''
def format_percent(num):
	return '{:.2f}%'.format(num)
