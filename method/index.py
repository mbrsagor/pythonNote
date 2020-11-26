def main_function():
    def inner_func():
        print("I am learning python from online.")

    return inner_func()


main_function()


def something(name, profession): return f"Hello this is {name} I'm a {profession}"
print(something("Sagor", "full-stack software engineer."))


def decorator(work):
    def child():
        print("Inside of decorator before calling the function.")
        work()
        print("Inside of the decorator after calling the function.")

    return child


@decorator
def get_decorator():
    print("I am another function")


get_decorator()


## Extra
def inner_function(name):
    def say_hello():
        return f"Hello there {name}!"

    return say_hello


@inner_function
def hello_something():
    print("I am something function")


function_instance = inner_function(hello_something())
print(function_instance())


def recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        result = n * recursive(n - 1)
        print(f"Result for {n} and factorial*{n - 1}= {result}")
        return result


recursive(5)


## Kwargs
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
