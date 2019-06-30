number = int(input("Give me factorial number:"))

fac = 1

for num in range(1, number + 1):
    fac *= num
print(f"Factorial of {number} = {fac}")
