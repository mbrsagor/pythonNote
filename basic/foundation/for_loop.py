for number in range(3):
    for number2 in range(4):
        print(f"({number}, {number2})")

items = [10, 4, 12]
total = 0

for item in items:
    total += item
print(total)

for i in items:
    print('*' * i)

for x in range(10):
    if x <= 3:
        print("I am counting:", x)

print('\n')

success = True
for a in range(10):
    print("it's ok")
    if success:
        break
    else:
        print("Stop!!")
