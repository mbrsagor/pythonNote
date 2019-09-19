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
