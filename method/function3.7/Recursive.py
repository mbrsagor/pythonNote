def recursive(number):
    """ Recursive """
    if number == 0:
        try:
            return 0
        except Exception as e:
            print(e)
    elif number == 1:
        return 1
    else:
        return number * recursive(number - 1)


print(recursive(5))


def factorial(n):
    """ Factorial """
    print("factorial has been called with n = " + str(n))
    if n == 1:
        return 1
    else:
        res = n * factorial(n - 1)
        print("intermediate result for ", n, " * factorial(", n - 1, "): ", res)
        return res


print(factorial(3))
