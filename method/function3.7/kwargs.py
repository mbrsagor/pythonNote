def languages(*args):
	""" 
		Here args use for 
	"""
	print(args)

languages("python")
languages("java")
languages("django")

print('\n')

def userInfo(**kwargs):
	print(kwargs)

userInfo(username='sagor', email='mbrsagor@gmail.com', password='sagor12345')
userInfo(username='sagor', email='mbrsagor@gmail.com', password='sagor12345')