from .base import BaseModel
from peewee import *

class Student(BaseModel):
	id = IntegerField()
	first_name = CharField()
	last_name = CharField()
	username = CharField()
	password = CharField()