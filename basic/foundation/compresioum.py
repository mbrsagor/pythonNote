number = 70

if 0 <= number <= 32:
    print("GPA: F")
elif 33 <= number <= 39:
    print("GPA: D")
elif 40 <= number <= 49:
    print("GPA: C")
elif 50 <= number <= 59:
    print("GPA: B")
elif 60 <= number <= 69:
    print("GPA: -A")
elif 70 <= number <= 79:
    print("GPA: A")
elif 80 <= number <= 100:
    if number == 100:
        print("Golden A+")
    else:
        print("GPA: A+")
else:
    print("Invalid Result")

"""
age = 170
if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")
"""

age = 20
something = "Eligible" if age >= 18 else "Not Eligible"
print(something)

personOne = "Sagor"
personTwo = "Sowrov"
theyAreBrother = True

if personOne == "Sagor" and personTwo == "Sowrov" and theyAreBrother:
    print("They are brother")
else:
    print("They are not brother")
