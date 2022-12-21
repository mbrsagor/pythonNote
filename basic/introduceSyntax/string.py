# String
first_name = "mbr"
last_name = "sagor"

full_name = f"Full name: {first_name} {last_name}"
print(full_name)

print(full_name.upper())
print(full_name.title())
print(len(full_name))

print(full_name.casefold())

name = "    Mbr Sagor"
print(name.istitle())
print(name.strip())
print(name.find("Sagor"))
print(name.replace("Mbr", "Mbr.").strip())

print("Mbr" in name)
print("Mbr." not in name)
print("Mbr." is name)

# Number
print(round(2.5))
print(round(abs(-30)))