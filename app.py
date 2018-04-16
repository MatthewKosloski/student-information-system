from router import Router
# from models import Student, Section, Course, Registration
# from peewee import *

def main():
	router = Router()

	# Generic routes
	router.add('/', {'controller': 'MainController'})
	router.add('/about', {'controller': 'AboutController'})
	router.add('/login', {'controller': 'LoginController'})
	router.add('/change-password', {'controller': 'PasswordController'})

	# Student routes
	router.add('/student', {'controller': 'StudentController'})
	router.add('/student/profile', {'controller': 'ProfileController'})
	router.add('/student/grades', {'controller': 'GradesController'})

	# Call '__init__' on the MainController
	router.dispatch('/')

if __name__ == '__main__':
	main()