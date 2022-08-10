info = {
"name": "mbr-sagor",
"age": 24,
"phone": 178880505,
"is_programmer": True
}

print(info.get("names", "Not found"))

print('\n')

for i in info.values():
    print(i)

user_input = input("Write something: ")
print(info[user_input])
