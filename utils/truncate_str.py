def truncate_str(str, to_length):
	return (str[:to_length] + '...') if len(str) > to_length else str