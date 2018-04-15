from views import SharedView
from .base import BaseController

class MainController(BaseController):

	def __init__(self, params):
		super().__init__(params)

	def index_action(self, payload):
		print('\n\nMainController')
		view = SharedView(self)
		view.render()

	def on_input(self, user_input):
		if user_input == 1:
			self.dispatch('/')
		elif user_input == 2:
			payload = {
				'to_about_controller': 'Hello, from MainController.'
			}
			self.dispatch('/about', payload)
