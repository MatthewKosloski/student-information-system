from peewee import *
from models import Student

class StudentController():

	def get_student(self, first_name):

		student = (Student.select()
			.where(Student.first_name == first_name)
			.get())
		
		return {
			'first_name': student.first_name,
			'last_name': student.last_name
		}