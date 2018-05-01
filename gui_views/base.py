import tkinter
from tkinter import messagebox

class BaseView():

	def __init__(self, controller, root, payload):
		self.__controller = controller
		self.__root = root
		self.__payload = payload
		self.__frame = tkinter.Frame(root, bg='white')

	def set_title(self, title_text):
		self.__root.title(title_text)

	def get_controller(self):
		return self.__controller

	def get_root(self):
		return self.__root

	def get_frame(self):
		return self.__frame

	def remove(self):
		self.__frame.grid_forget()

	def show_error_message(self, message):
		messagebox.showerror('Error', message)

	def clear_menu(self):
		empty_menu = tkinter.Menu(self.__root)
		self.__root.config(menu=empty_menu)


