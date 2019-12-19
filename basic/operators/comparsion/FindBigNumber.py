number1 = 20
number2 = 40
number3 = 50

if number1 > number2:
    find_big_number = number1
else:
    find_big_number = number2

if number3 > find_big_number:
    find_big_number = number3

print(f"Maximum big number is: {find_big_number}")

find_small_number = 0
if number1 < number2 and number1 < number3:
    find_small_number = number1

print(f"Minimum small number is: {find_small_number}")
