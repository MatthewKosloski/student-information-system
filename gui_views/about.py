import tkinter
from .base import BaseView

class AboutView(BaseView):

	def __init__(self, controller, root, payload):
		super().__init__(controller, root, payload)
		self.set_title('Student Information System — About')
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
		self.label = tkinter.Label(self.get_frame(), text='About', font=('Helvetica Neue', 16), anchor='w')
		self.text = tkinter.Text(self.get_frame())
		self.btn = tkinter.Button(self.get_frame(), text='Back', command=self.go_back)

	def render(self, payload):
		print('AboutView received payload:', payload)
		self.get_frame().grid()

		self.label.grid(row=0, sticky=tkinter.W+tkinter.E)
		self.text.grid(row=1)
		self.btn.grid(row=2, sticky=tkinter.W)
		self.text.insert(tkinter.END, 'Software built by Logan Miller, Matthew Kosloski, and Paul Barnes.')
		self.text.config(state=tkinter.DISABLED, font=('Helvetica Neue', 14), height=1)

	def go_back(self):
		self.clear_menu()
		self.remove()
		self.get_controller().go_back()

	def on_label1(self):
		print('Label 1 chosen')
