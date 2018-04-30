from .base import BaseController
from views import NameSelectionView
from models import Course
from routes import *

class NameSelectionController(BaseController):

	def __init__(self, router, payload):
		super().__init__(router, payload)

		self.__view = NameSelectionView(self)
		self.__view.render(payload)

	'''
		Returns a boolean indicating if
		a course has the provided name.

		@param name {str}
		@return {bool}
	'''
	def is_valid_name(self, name):
		query = (Course
			.select()
			.where(Course.name == name))
		return query.exists()

	def on_name_selection(self, name):
		if self.is_valid_name(name):
			self.__view.set_name_status(True)
			payload = {
				'type': self.get_payload()['type'],
				'id': self.get_payload()['id'],
				'course_name': name
			}
			self.dispatch(SEARCH_RESULTS_ROUTE, payload)
		else:
			self.__view.print_message(f'No course named {name} exists.')