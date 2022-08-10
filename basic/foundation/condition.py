text = "My name is mbr sagor"

if "sagor" in text:
    print("Welcome")
else:
    print("Not found")

is_present = True
is_absent = False

if is_present:
    print("He is good boy")
elif is_absent:
    print("He is bad boy")
else:
    print("Let me call him")

price = 1000000
has_good_credit = True

if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f"Down Payment: ${down_payment}")

has_high_income = False
has_high_credit = True

if has_high_income or has_high_credit:
    print("Eligible for loan")

has_high_credit = True
has_criminal_record = False

if has_high_credit and not has_criminal_record:
    print("Something... valid loan")
else:
    print("Invalid loan")

temperature = 30
if temperature >= 20:
    print("it's a hot day")
else:
    print("it's a cool day")

name = "Bozlur Rosid Sagor"
if len(name) <= 5:
    print("Name must be at least 5 characters")
elif len(name) >= 10:
    print("Name is too long")
else:
    print("Nice name")
