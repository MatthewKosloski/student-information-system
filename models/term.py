from .base import BaseModel
from peewee import *

class Term(BaseModel):
	id = IntegerField()
	title = CharField()
	abbreviation = CharField()
