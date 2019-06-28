items = {"Phone": "Samsung", "Price": 35000, "Model": "S17i"}
print(items)

print(items.keys())
print(items.values())
print(items['Phone'])

_item =items['phone'] = "Iphone"
print(_item)

print(items.get('Prices', 'Not found'))