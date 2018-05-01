from models import Term

'''
	Queries the database for the title
	column in terms with a specific ID.

	@return {str}
'''
def get_term_name(term_id):
	return middleware(query(term_id))

def query(term_id):
	query = (Term
		.select(Term.title)
		.where(Term.id == term_id)
		.dicts())

	return query

'''
	Processes the get_term_name query by
	returning the first result.

	@param query
	@return {str}
'''
def middleware(query):
	term_name = []
	for item in query:
		term_name.append(item['title'])
	return term_name[0]
