from router import Router
from models import Student
from peewee import *

def main():
	router = Router()

	router.add('/', {
		'controller': 'MainController', 
		'action': 'index_action'
	})

	router.add('/about', {
		'controller': 'AboutController', 
		'action': 'index_action'
	})

	router.add('/login', {
		'controller': 'LoginController', 
		'action': 'index_action'
	})

	router.add('/student/home', {
		'controller': 'StudentHomeController',
		'action': 'index_action'
	})

	# Call 'index_action' on the MainController
	router.dispatch('/')

	# def get_account(model, username):
	# 	try:
	# 		query = (model
	# 			.select()
	# 			.where(getattr(model, 'username') == username)
	# 			.get())

	# 		return query
	# 	except DoesNotExist:
	# 		raise ValueError(('Either the username is incorrect' +
	# 			' or the account doesn\'t exist!'))

	# db_account = get_account(Student, 'mkosloski97')
	# print(db_account.first_name)

if __name__ == '__main__':
	main()