n = 1
total = 0
while n <= 100:
    total += n
    print(n, end=' ')
    n += 1
print('\n')
print(f"Total calculation of loop number is: {total}")

num = 1
while num <= 10:
    if num % 2 == 0:
        print(num)
    num += 1
else:
    print("Event number is over.")

_number = int(input("Enter your number: "))
_count = 1

while _count <= 10:
    result = _number * _count
    print(f"{_number} x {_count} = {result}")
    _count += 1
