# number = 0
#
# while number <= 5:
#     print(number)
#     number += 1
#
# start_number = int(input("Enter start from: "))
# end_number = int(input("Enter end from: "))
# while start_number <= end_number:
#     print("*" * start_number)
#     start_number += 1

"""

secret_number = 9
guess_count = 0
guess_limit = 3

while guess_count < guess_limit:
    guess = int(input("Guess: "))
    guess_count += 1
    if guess == secret_number:
        print("You are lucky :) ")
        break
else:
    print("Sorry you failed :|")

"""

numbers = 10
while numbers > 0:
    numbers -= 1
    print("Hello", numbers)

print('\n')

number = 0
while number < 10:
    number += 1
    print("I am counting:", number)

while True:
    if number <= 5:
        number += 1
        print(number)
