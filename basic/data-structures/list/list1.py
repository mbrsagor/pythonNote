"""
There are kind of some list operation:
1) Replace/Update
2) Insert
3) Sort
4) Extends
5) Delete
6) Append
7) Reverse
8) Remove
9) Pop
"""

names = ['sagor', 'ohi', 'shanto', 'someone']
names.reverse()
print(names)
names.sort()
print(names)

names.append('showrove')
print(names)

students = ['medha', 'ritu', 'biva', 'eiva', 'ekera', 'fariya']
names.extend(students)
print(names)

for name in names:
    print(name.upper())

names.insert(0, 'Ruble')
print(names)

numbers = [10, 20, 11, 13, 5, 1, 8]
print(numbers)
numbers.sort()
print(numbers)

languages = ['python', 'java', 'c', 'javascript', 'go', 'c++']
print(languages)
languages.sort()
print(languages)

del names[4]
print(names)

languages.append('PHP')
print(languages)
languages.insert(0, 'HTML')
print(languages)
languages.reverse()
print(languages)

inline_calculate = [num ** 2 for num in [2, 4, 10]]
print(inline_calculate)
