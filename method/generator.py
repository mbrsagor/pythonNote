def topten():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5
    yield 5


instance = topten()
print(instance.__next__())
print(instance.__next__())
print(instance.__next__())
print(instance.__next__())
print(instance.__next__())

print('\n')


def square():
    n = 1

    while n <= 10:
        sq = n * n
        yield sq
        n += 1


sq_instance = square()
print(sq_instance)

for i in sq_instance:
    print(i)
