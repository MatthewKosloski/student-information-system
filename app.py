from controllers import StudentController

name = input('Enter your name: ')
student_controller = StudentController()

print(student_controller.get_student(name))