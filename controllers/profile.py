from .base import BaseController
from views import ProfileView
from routes import HOME_ROUTE
from models import Student
import utils

class ProfileController(BaseController):

	def __init__(self, router, payload):
		super().__init__(router, payload)

		self.__view = ProfileView(self)
		self.__view.render(
			self.process_get_student_profile(self.get_student_profile()))

	'''
		Queries the database for the Student
		profile fields (e.g., first name, last
		name, address, phone number, etc.)

		@return {dict} Values to be displayed
	'''
	def get_student_profile(self):
		student_id = self.get_payload()['id']
		query = (Student
			.select(
				Student.id,
				Student.username,
				Student.first_name,
				Student.last_name,
				Student.sex,
				Student.date_of_birth,
				Student.age,
				Student.address_street,
				Student.address_city,
				Student.address_state,
				Student.address_zip_code,
				Student.phone_number,
				Student.email
			).where(Student.id == student_id)
			.dicts())

		return query

	'''
		Processes the results of the 
		get_student_profile query before handing
		it off to the view.

		@param query {Student}
		return {dict}
	'''
	def process_get_student_profile(self, query):
		profile = []
		for student in query:
			profile.append({
				'full_name': utils.format_name(student['first_name'], student['last_name']),
				'sex': utils.get_sex(student['sex']),
				'date_of_birth': utils.to_mm_dd_yyyy(student['date_of_birth']),
				'phone_number': utils.format_phone_number(student['phone_number']),
				'age': str(student['age']),
				'id': str(student['id']),
				'address_zip_code': str(student['address_zip_code']),
				'username': student['username'],
				'address_street': student['address_street'],
				'address_city': student['address_city'],
				'address_state': student['address_state'],
				'email': student['email']
			})
		return profile[0]

	'''
		Handle the user's choice and redirect
		them to the appropriate view.
		
		@param choice {int} Number corresponding to
		the view in the ordered list menu.
		@param meta {Any} The meta value associated
		with the choice.
	'''
	def on_choice_selection(self, choice, meta):
		if choice == 1:
			self.go_back()
		else:
			self.dispatch(HOME_ROUTE)


