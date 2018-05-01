'''
	Converts a date object to the
	mm/dd/yyyy syntax.

	@param date {date}
	@return {str}
'''
def to_mm_dd_yyyy(date):
	return date.strftime('%m/%d/%Y')