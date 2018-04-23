from gui_views import AboutView
from .base import BaseController

class AboutController(BaseController):

	def __init__(self, router, root, payload):
		super().__init__(router, root, payload)
		
		print('AboutController!')
		self.__view = AboutView(self, root, payload)
		self.__view.render(payload)

