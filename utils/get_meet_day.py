'''
	Maps an integer to a day of the week.

	@param day_int {int}
	@return {str}
'''
def get_meet_day(day_int):
	meet_days = ['', 'M', 'T', 'W', 'R', 'F', 'MWF', 'TR']
	return meet_days[day_int]