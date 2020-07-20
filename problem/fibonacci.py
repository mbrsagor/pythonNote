"""
The fibonacci example
1 + 2 + 3 + 4+ 5 = result
"""

def fibonacci(number):
    if number == 0 or number == 1:
        return number
    else:
        return number + fibonacci(number - 1)

print(fibonacci(5))
