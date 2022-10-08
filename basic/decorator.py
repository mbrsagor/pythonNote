def say_hello(func):
    def welcome():
        print("Hello everyone, how are you?")
        func()
        print("Welcome, to your website")

    return welcome()


@say_hello
def say_something():
    print("I'm calling to say something decorator method")
