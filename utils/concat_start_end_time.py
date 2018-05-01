import utils

'''
	Concatenates and truncates a starting
	and ending time.

	@param start_time {time}
	@param end_time {time}
	@param {str}
'''
def concat_start_end_time(start_time, end_time):
	start_formatted = utils.to_hh_mm(start_time)
	end_formatted = utils.to_hh_mm(end_time)

	time = f'{start_formatted} to {end_formatted}'
	return utils.truncate_str(time, 25)