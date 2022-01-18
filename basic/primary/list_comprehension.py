fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
numbers = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]

newlist = [x for x in fruits]
print(newlist)

list_condition = [fruit for fruit in fruits if "a" in fruit]
print(list_condition)


even_number = [num for num in numbers if num % 2 == 0]
print(even_number)

result = [n * 2 for n in numbers]
print(result)

items = []
_item = [items.append(n) for n in numbers]
print(items)
