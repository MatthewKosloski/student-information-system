from gui_views import StudentView
from .base import BaseController

class StudentController(BaseController):

	def __init__(self, router, root, payload):
		super().__init__(router, root, payload)
		
		self.__view = StudentView(self, root, payload)
		self.__view.render(payload)

