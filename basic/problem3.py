def display(L, nagative=True, odd=True):
    for n in L:
        if n < 0 and nagative is False:
            continue
        if n % 2 !=0 and odd is False:
            continue
        print(n, end=' ')
    print()
    

numbers = [12, -1, 3, 6, 8, 9, 38, -3, 34, -4]

display(numbers, True, False)
display(numbers, False)
display(numbers, True, odd=False)
display(numbers, True, nagative=False)
display(numbers, nagative=False, odd=False)
