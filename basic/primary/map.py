animals = ['dog', 'cat', 'parrot', 'rabbit']
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]


# Example: 1
def calculation(num):
    return num + 5

results = map(calculation, li)
print(results)

# converting map object to set
numbersSquare = set(results)
print(numbersSquare)

# Example: 2
animals_list = list(map(lambda animal:animal, animals))
print(animals_list)


# Example: 2
numbers = list(map(lambda n: n * 2, li))
print(numbers)
