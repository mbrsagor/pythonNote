def factorial(start):
    number = 1

    if (start == 0):
        print("The factorial is 0 is 1")

    elif (start < 0):
        print("Sorry, factorial does not exist for negative numbers")

    for fact in range(1, start + 1):
        number = fact * number
        print(f"The number of {fact} factorial  is {number}")


factorial(5)
