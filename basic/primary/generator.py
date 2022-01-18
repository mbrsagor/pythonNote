def infinite_sequence():
    num = 2
    while True:
        yield num
        if num % 2 == 0:
            num += 2


gen = infinite_sequence()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

print('\n')


### Example 2:
def status():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5
    yield 6

for val in status():
    print(val)

print('\n')

# Example 3:
def gen():
    print('First item')
    yield 10

    print('Second item')
    yield 20

    print('Third item')
    yield 30


print(next(gen()))


for keyVal in gen():
    print(keyVal)
