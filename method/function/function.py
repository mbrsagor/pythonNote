"""
Python function has three step:
1) Function define
2) Function name and paramitter
3) Function body

"""


def my_function(n1, n2, n3):
    return n1 + n2 + n3


n1 = int(input('Enter first integer number'))
n2 = int(input('Enter second integer number'))
n3 = int(input('Enter last integer number'))
output = my_function(n1, n2, n3)
print(output)

print('\n')


def function(*myList):
    for _list in myList:
        print(_list)
    return None


function(20, 30, 20, 54, 38, 28, 10, 5)
