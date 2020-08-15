number = 70

if (number >= 0 and number <= 32):
    print("GPA: F")
elif (number >= 33 and number <= 39):
    print("GPA: D")
elif (number >= 40 and number <= 49):
    print("GPA: C")
elif (number >= 50 and number <= 59):
    print("GPA: B")
elif (number >= 60 and number <= 69):
    print("GPA: -A")
elif (number >= 70 and number <= 79):
    print("GPA: A")
elif (number >= 80 and number <= 100):
    if (number == 100):
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

