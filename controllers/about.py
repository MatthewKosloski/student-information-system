from views import SharedView
from .base import BaseController

class AboutController(BaseController):

	def __init__(self, params):
		super().__init__(params)

	def index_action(self, payload):
		print('\n\nAboutController')
		view = SharedView(self)
		view.render()

	def on_input(self, user_input):
		if user_input == 1:
			payload = {
				'to_main_controller': 'Hello, from AboutController.'
			}
			self.dispatch('/', payload)
		elif user_input == 2:
			self.dispatch('/about')


