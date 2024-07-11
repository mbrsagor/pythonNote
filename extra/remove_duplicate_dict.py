# Original list with duplicate dictionaries
original_list = [
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob', 'age': 30},
    {'name': 'Alice', 'age': 25},  # duplicate
    {'name': 'Charlie', 'age': 35}
]

print(original_list)

unique_list = [dict(t) for t in {tuple(d.items()) for d in original_list}]
print(unique_list)
