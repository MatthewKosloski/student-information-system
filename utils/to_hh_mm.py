'''
	Converts a time object to the hh:mm
	syntax (including AM or PM).

	@param time {time}
	@return {str}
'''
def to_hh_mm(time):
	return time.strftime('%I:%M %p')