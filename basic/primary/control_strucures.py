"""
There are 3 types of control stracture:
1) Sequential control
2) Selection control
3) Interative control

"""

# sequential control
print("Say something")
print("Hello I am sagor...")
print("Could you please tell me something...")

# Selection control
number = int(input("Enter any kind of number: "))
if number <= 10:
    print(f"The {number} is less then 10")
else:
    print("False answer.. Try again later....")

# Interative control

num = 0
while num <= 10:
    if num % 2 == 0:
        print(num)
    num += 1
