import tkinter
from tkinter import ttk
from .base import BaseView

class LoginView(BaseView):

	def __init__(self, controller, root, payload):
		super().__init__(controller, root, payload)
		self.set_title('Student Information System — Home')
		self.create_menu()
		self.init_widgets()

	def create_menu(self):
		root = self.get_root()

		menu = tkinter.Menu(root)
		root.config(menu=menu)

		about = tkinter.Menu(menu)
		menu.add_cascade(label='About', menu=about)

		about.add_command(label='About', command=self.go_about)	


	def init_widgets(self):
		self.title = tkinter.Label(
			self.get_frame(), \
			text='Login', \
			font=('Helvetica Neue', 16), \
			anchor='w')

		self.account_var = tkinter.IntVar()
		self.account_student = tkinter.Radiobutton(
			self.get_frame(), \
			text='Student', \
			variable=self.account_var, \
			value=1)
		self.account_teacher = tkinter.Radiobutton(
			self.get_frame(), \
			text='Teacher', \
			variable=self.account_var, \
			value=2)

		self.username_label = tkinter.Label(self.get_frame(), text='Username:')
		self.username_entry = tkinter.Entry(self.get_frame())

		self.password_label = tkinter.Label(self.get_frame(), text='Password:')
		self.password_entry = tkinter.Entry(self.get_frame(), show='*')

		self.btn = tkinter.Button(
			self.get_frame(), \
			text='Login', \
			command=self.on_login
		)

	def render(self, payload):
		print('LoginView received payload:', payload)
		self.get_frame().grid()

		self.title.grid(row=0, sticky=tkinter.W+tkinter.E)
		self.account_student.grid(row=1)
		self.account_teacher.grid(row=1, column=2)
		self.username_label.grid(row=2)
		self.username_entry.grid(row=2, column=2)
		self.password_label.grid(row=3)
		self.password_entry.grid(row=3, column=2)
		self.btn.grid(row=4)

	def go_about(self):
		self.remove()
		self.get_controller().go_about()

	def on_login(self):
		self.get_controller().login(
			self.account_var.get(), \
			self.username_entry.get(), \
			self.password_entry.get())
