list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
zipped = zip(list1, list2)
print(list(zipped))
# Output: [(1, 'a'), (2, 'b'), (3, 'c')]


list1 = [1, 2, 3]
list2 = ['a', 'b']
zipped = zip(list1, list2)
print(list(zipped))
# Output: [(1, 'a'), (2, 'b')]  # Stops at the shortest iterable


zipped = [(1, 'a'), (2, 'b'), (3, 'c')]
unzipped = zip(*zipped)
print(list(unzipped))
# Output: [(1, 2, 3), ('a', 'b', 'c')]

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
for num, char in zip(list1, list2):
    print(f"Number: {num}, Character: {char}")
# Output:
# Number: 1, Character: a
# Number: 2, Character: b
# Number: 3, Character: c


list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
list3 = [True, False, True]
zipped = zip(list1, list2, list3)
print(list(zipped))
# Output: [(1, 'a', True), (2, 'b', False), (3, 'c', True)]


keys = ['name', 'age', 'city']
values = ['Alice', 25, 'New York']
dictionary = dict(zip(keys, values))
print(dictionary)
# Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}

