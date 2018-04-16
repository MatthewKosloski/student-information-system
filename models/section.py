from .base import BaseModel
from .instructor import Instructor
from .course import Course
from peewee import *

class Section(BaseModel):
	id = IntegerField()
	instructor_id = ForeignKeyField(Instructor)
	course_id = ForeignKeyField(Course)
	number = IntegerField()
	capacity = IntegerField()
	meet_day = IntegerField()
	meet_location = CharField()
	meet_time_start = TimeField()
	meet_time_end = TimeField()
	start_date = DateField()
	end_date = DateField()
	type = IntegerField()