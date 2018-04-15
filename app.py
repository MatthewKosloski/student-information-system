from router import Router

def main():
	router = Router()

	router.add('/', {
		'controller': 'MainController', 
		'action': 'index_action'
	})

	router.add('/about', {
		'controller': 'AboutController', 
		'action': 'index_action'
	})

	# Call 'index_action' on the MainController
	router.dispatch('/')

if __name__ == '__main__':
	main()