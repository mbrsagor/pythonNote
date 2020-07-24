def fib(_start):
    first = 0
    last = 1

    if _start == 1:
        print(first)
    else:
        print(first)
        for start in range(_start):
            result = first + last
            first = last
            last = result
            print(result)


fib(10)

print("\n")


def fibo(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
        print()


fibo(10)
