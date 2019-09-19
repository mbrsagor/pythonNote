items = {"Phone": "Samsung", "Price": 35000, "Model": "S17i"}

print(items.keys())
print(items.values())
print(items['Phone'])

_item = items['phone'] = "Iphone"

print(items.get('Prices', 'Not found'))

print(f"My Phone Name is {items['Phone']}")

items["Color"] = "Black"

for item in items.items():
    print(item)

print(f"My phone color is: {items.get('Color')}")
print(items)
del items['Phone']
