import tkinter
from gui_router import GUIRouter
from routes import (
	HOME_ROUTE,
	ABOUT_ROUTE,
	STUDENT_ROUTE # = '/student'
)

def main():

	class App:

		def __init__(self):

			self.root = tkinter.Tk()
			self.root.geometry('600x500')
			self.root.title('Student Information System')

			router = GUIRouter(self.root)

			# Generic routes
			router.add(HOME_ROUTE, 'LoginController')
			router.add(ABOUT_ROUTE, 'AboutController')

			# Student routes
			router.add(STUDENT_ROUTE, 'StudentController')

			router.dispatch(HOME_ROUTE)

			tkinter.mainloop()

	app = App()

main()