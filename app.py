from router import Router
from routes import (
	HOME_ROUTE,
	ABOUT_ROUTE,
	LOGIN_ROUTE,
	CHANGE_PASSWORD_ROUTE,
	STUDENT_ROUTE,
	STUDENT_PROFILE_ROUTE,
	STUDENT_GRADES_ROUTE
)

def main():
	router = Router()

	# Generic routes
	router.add(HOME_ROUTE, 'MainController')
	router.add(ABOUT_ROUTE, 'AboutController')
	router.add(LOGIN_ROUTE, 'LoginController')
	router.add(CHANGE_PASSWORD_ROUTE, 'PasswordController')

	# Student routes
	router.add(STUDENT_ROUTE, 'StudentController')
	router.add(STUDENT_PROFILE_ROUTE, 'ProfileController')
	router.add(STUDENT_GRADES_ROUTE, 'GradesController')

	# Call '__init__' on the MainController
	router.dispatch(HOME_ROUTE)

if __name__ == '__main__':
	main()