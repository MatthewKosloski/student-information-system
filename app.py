from router import Router
# from models import Student, Section, Course, Registration
# from peewee import *

def main():
	router = Router()

	# Generic routes
	router.add('/', 'MainController')
	router.add('/about', 'AboutController')
	router.add('/login', 'LoginController')
	router.add('/change-password', 'PasswordController')
	router.add('/help', 'HelpController')

	# Student routes
	router.add('/student', 'StudentController')
	router.add('/student/profile', 'ProfileController')
	router.add('/student/grades', 'GradesController')

	# Call '__init__' on the MainController
	router.dispatch('/')

if __name__ == '__main__':
	main()