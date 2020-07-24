# How to calculate two number
add = lambda num, num2: num + num2
print(add(30, 20))


# lambda function using custom function
def calculate_number(n):
    return lambda num: n * num


cn = calculate_number(5)
print(cn(5))

make_full_name = lambda first_name, last_name: f"Full Name: {first_name} {last_name}"

full_name = make_full_name("Mbr", "Sagor")
print(full_name)
