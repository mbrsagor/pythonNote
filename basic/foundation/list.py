numbers = [40, 10, 90, 20, 30, 70, 80, 30]
print(max(numbers))
numbers.sort()
print(numbers)

print('\n')

empty_list = []

for number in numbers:
    if number is not empty_list:
        empty_list.append(number)
        print(empty_list)
