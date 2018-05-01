from models import Section, Course
from utils import get_section_str

'''
	Returns the name of the section (e.g., MATH-2100)
	based on a provided section id.

	@param section_id {int}
	@return {str}
'''
def get_section_name(section_id):
	return middleware(query(section_id))		

def query(section_id):
	query = (Section
			.select(Section.number, Course.name, Course.title)
			.join(Course, on=(Section.course_id == Course.id))
			.where(Section.id == section_id)
			.dicts())

	return query

def middleware(query):
	return [get_section_str(
		section['name'], 
		section['title'], 
		section['number']) for section in query][0]