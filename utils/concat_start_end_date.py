import utils

'''
	Concatenates and truncates a starting
	and ending date.

	@param start_date {date}
	@param end_date {date}
	@param {str}
'''
def concat_start_end_date(start_date, end_date):
	start_formatted = utils.to_mm_dd_yyyy(start_date)
	end_formatted = utils.to_mm_dd_yyyy(end_date)

	date = f'{start_formatted} to {end_formatted}'
	return utils.truncate_str(date, 25)