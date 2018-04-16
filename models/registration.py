from .base import BaseModel
from .student import Student
from .section import Section
from peewee import *

class Registration(BaseModel):
	student_id = ForeignKeyField(Student)
	section_id = ForeignKeyField(Section)
	letter_grade = IntegerField()
	percent_grade = FloatField()
