class SharedView():

	def __init__(self, controller):
		self.__controller = controller

	def render(self):
		print()
		print()
		print('This view is used by both the MainController and AboutController.')
		print()
		print('1. Go to MainController')
		print('2. Go to AboutController')
		
		self.__controller.on_input(int(input('> ')))
