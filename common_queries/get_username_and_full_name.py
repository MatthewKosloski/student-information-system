import peewee

'''
	Get the username, firstname, and lastname
	from the account who is associated with the
	provided ID.

	@param model {BaseModel} Type of model to query
	@param id {int} ID of the account
	@return {dict} A dictionary containing the username
	and full name of the account.
'''
def get_username_and_full_name(model, id):
	return middleware(query(model, id))

def query(model, id):
	query = (model
		.select(getattr(model, 'username'), 
			getattr(model, 'first_name'), 
			getattr(model, 'last_name'))
		.where(getattr(model, 'id') == id)
		.dicts())

	return query

def middleware(query):
	try:
		result = list(query)[0]
		return {
			'username': result['username'],
			'full_name': f'{result["first_name"]} {result["last_name"]}'
		}
	except IndexError:
		raise ValueError('Invalid ID provided to get_username_and_full_name.')