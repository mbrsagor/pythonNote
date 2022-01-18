def make_pretty(func):
    def inner():
        print("I got decorated")
        func()

    return inner


@make_pretty
def ordinary():
    print("I am ordinary")


ordinary()


# V2
def uppercase_decorator(function):
    def wrapper():
        content = function().upper()
        return content
    return wrapper


@uppercase_decorator
def say_hello():
    return "hello there, this is a bozlur rosid sagor"


print(say_hello())
