from .base import BaseModel
from peewee import *

class Student(BaseModel):
	id = IntegerField()
	first_name = CharField()
	last_name = CharField()
	username = CharField()
	password = CharField()
	sex = IntegerField()
	date_of_birth = DateField()
	age = IntegerField()
	address_street = CharField()
	address_city = CharField()
	address_state = CharField()
	address_zip_code = IntegerField()
	address_country = CharField()
	phone_number = IntegerField()
	email = CharField()