from router import Router
from routes import *

def main():
	router = Router()

	# Generic routes
	router.add(HOME_ROUTE, 'MainController')
	router.add(ABOUT_ROUTE, 'AboutController')
	router.add(LOGIN_ROUTE, 'LoginController')
	router.add(CHANGE_PASSWORD_ROUTE, 'PasswordController')

	# Search routes
	router.add(SEARCH_ROUTE, 'SearchController')
	router.add(SEARCH_SELECT_TERM_ROUTE, 'TermSelectionController')
	router.add(SEARCH_SELECT_NAME_ROUTE, 'NameSelectionController')
	router.add(SEARCH_RESULTS_ROUTE, 'SectionsController')

	# Student routes
	router.add(STUDENT_ROUTE, 'StudentController')
	router.add(STUDENT_PROFILE_ROUTE, 'ProfileController')
	router.add(STUDENT_GRADES_SELECT_TERM_ROUTE, 'TermSelectionController')
	router.add(STUDENT_GRADES_TERM_GRADES_ROUTE, 'GradesController')
	router.add(STUDENT_SCHEDULE_SELECT_TERM_ROUTE, 'TermSelectionController')
	router.add(STUDENT_SCHEDULE_TERM_SCHEDULE_ROUTE, 'SectionsController')
	router.add(STUDENT_REGISTER_ROUTE, 'RegisterController')

	# Instructor routes
	router.add(INSTRUCTOR_ROUTE, 'InstructorController')
	router.add(INSTRUCTOR_INPUT_GRADES_ROUTE, 'InputGradesController')
	router.add(INSTRUCTOR_ROSTER_SELECT_TERM_ROUTE, 'TermSelectionController')
	router.add(INSTRUCTOR_ROSTER_SELECT_SECTION_ROUTE, 'SectionSelectionController')
	router.add(INSTRUCTOR_ROSTER_SECTION_ROSTER_ROUTE, 'RosterController')

	# Registrar routes
	router.add(REGISTRAR_ROUTE, 'RegistrarController')
	router.add(REGISTRAR_REGISTER_STUDENT_SELECT_ID_ROUTE, 'StudentIDSelectionController')
	router.add(REGISTRAR_REGISTER_STUDENT_ROUTE, 'RegisterController')

	# Call '__init__' on the MainController
	router.dispatch(HOME_ROUTE)

if __name__ == '__main__':
	main()