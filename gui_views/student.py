import tkinter
from .base import BaseView

class StudentView(BaseView):

	def __init__(self, controller, root, payload):
		super().__init__(controller, root, payload)
		self.set_title('Student Information System — Student')
		self.create_menu()
		self.init_widgets()

	def create_menu(self):
		root = self.get_root()

		menu = tkinter.Menu(root)
		root.config(menu=menu)

		file = tkinter.Menu(menu)
		menu.add_cascade(label='File', menu=file)

		file.add_command(label='Label1', command=self.on_label1)

	def init_widgets(self):
		self.label = tkinter.Label(self.get_frame(), text='StudentView', font=('Helvetica Neue', 16), anchor='w')

	def render(self, payload):
		print('StudentView received payload:', payload)
		self.get_frame().grid()

		self.label.grid(row=0, sticky=tkinter.W+tkinter.E)

	def go_back(self):
		self.clear_menu()
		self.remove()
		self.get_controller().go_back()

	def on_label1(self):
		print('Label 1 chosen')
