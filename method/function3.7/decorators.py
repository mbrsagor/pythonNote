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


#
# def inner_function(name):
#     def say_hello():
#         return f"Hello there {name}!"
#
#     return say_hello
#
#
# @inner_function
# def hello_something():
#     print("I am something function")
#
#
# function_instance = inner_function(hello_something())
# print(function_instance())
#
#
# def recursive(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         result = n * recursive(n - 1)
#         print(f"Result for {n} and factorial*{n - 1}= {result}")
#         return result
#
#
# recursive(5)
