'''
	Maps a percent to an integer
	representing a letter grade (1 = A,
	2 = B ... 5 = F).

	@param percent_grade {float}
	@return {int}
'''
def get_letter_grade_int(percent_grade):
	if percent_grade >= 90: # 90-100
		return 1
	elif percent_grade >= 80 and percent_grade < 90: # 80-89
		return 2
	elif percent_grade >= 70 and percent_grade < 80: # 70-79
		return 3
	elif percent_grade >= 60 and percent_grade < 70: # 60-69
		return 4
	else: # 0-59
		return 5