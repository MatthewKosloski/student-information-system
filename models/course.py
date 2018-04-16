from .base import BaseModel
from peewee import *

class Course(BaseModel):
	id = IntegerField()
	name = CharField()
	title = CharField()
	credit_hours = IntegerField()
	description = TextField()