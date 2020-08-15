result = lambda num, num2: num + num2
print(f"Total result is: {result(20, 30)}")

filter_instance = filter(lambda number: number % 2 == 0, range(1, 11))
print(filter_instance)

filter_instance = list(filter(lambda number: number % 2 == 0, range(1, 11)))
print(filter_instance)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
lambda_filter = filter(lambda x: x % 2 == 0, numbers)
print(lambda_filter)

"""
# Here filter instance using `list` is support python-3 
# And last one function using for python 2.7
"""
