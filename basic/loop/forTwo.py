stop = True

for number in range(5):
    print("I am counting ", number)
    if stop:
        print("Stop the loop from here")
        break

for num1 in range(10):
    for num2 in range(num1):
        print(num2, end="")
    print()
