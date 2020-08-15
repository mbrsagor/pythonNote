"""
There are two membership operator:
`Here, basically the membership operator return true or false`
1) in
2) not in
"""

in_example = 3 in [1, 2, 3, 4, 5, 10]
print(in_example)

not_in_example = 60 not in [1, 2, 3, 4, 5, 10]
print(not_in_example)

"""
Boolean operator three element:
1) and
2) or
3) not
"""

example = 50 < 60 and 10 == 10
print(example)

example2 = 12 > 15 and 7 == 7
print(example2)

example3 = 20 <= 10 or 40 == 40
print(example3)

example4 = 15 > 10 and 5 < 7 or 30 == 300
print(example4)

num1 = 300
num2 = 3000
result = not num1 > num2
print(result)

try:
    division_number = 20 / 0
    print(division_number)
except ZeroDivisionError as e:
    print(e)
