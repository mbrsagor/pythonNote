"""
first_name = "mbr"
last_name = "sagor"

message = first_name+"("+last_name+")"+"is a coder"
print(message)


mes = f'{first_name} ({last_name}) is a coder'
print(mes)


print(len(message))
print(message.upper())

print(message.find('d'))

name = "mbr sagor"
print(name.replace('mbr', 'Md'))

print('sagor' in name)

"""

li = [20, 40, 10, 30]
total = 0

for l in li:
    total += l
print(total)

first_name = "mbr"
last_name = "sagor"

full_name = f"{first_name} {last_name}"
print("Full Name: " + full_name)

text1 = "python programming course"

print("course" in text1)
print("javascript" not in text1)

print('\n')
