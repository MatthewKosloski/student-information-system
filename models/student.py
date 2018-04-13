from peewee import *
from .base import BaseModel

class Student(BaseModel):
	first_name = CharField()
	last_name = CharField()
	username = CharField()
	password = CharField()