from router import Router
from routes import *
from table import Table

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
	router.add(STUDENT_SCHEDULE_ROUTE, 'ScheduleController')

	# Call '__init__' on the MainController
	router.dispatch(HOME_ROUTE)

	# my_table = Table()
	# my_table.add_columns(['Course', 'Section Number', 'Instructor'])
	# my_table.add_row('CPSC-3110', '1', 'Freddie Kato')

	# print('Length of longest field:', my_table.get_longest_field_len())
	# print('Length of longest column:', my_table.get_longest_column_len())
	# print('Largest of the two:', my_table.get_longest())

	# print(my_table)

	# row = ('Hello', 'World')
	# formatted_str = ('{:<{width}} '.format(width=5)) * 2
	# print(formatted_str.format('Hello', 'World'))

	# row = ('Adam', 'Lippert')
	# row_len = len(row)
	# width = 15
	# formatted_str = '{:<{width}}'.format(width=width) * row_len
	# print(formatted_str.format(*row))


if __name__ == '__main__':
	main()