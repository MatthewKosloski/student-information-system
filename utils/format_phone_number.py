'''
	Formats a U.S., 10-digit phone number
	by adding hypthens in between the numbers.

	@param phone_number {str} 10-digit phone number
	@return {str}
'''
def format_phone_number(phone_number):
	num_str = str(phone_number)

	if len(num_str) == 10:
		return f'{num_str[:3]}-{num_str[3:6]}-{num_str[6:]}'
	else:
		return num_str