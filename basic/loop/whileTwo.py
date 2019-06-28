item = 0

while item < 10:
    if item == 2:
        break
    print(item)
    item += 1

print('\n')

number = 11
while number > 0:
    print(number)
    number //= 2

code_runner = ""
while code_runner != "exit":
    code_runner = input("> ")
    print(code_runner)
