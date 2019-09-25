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

aliens = []

for alien_number in range(0, 30):
    new_alien = {"color": "red", "model": 560}
    aliens.append(new_alien)

for alien in aliens:
    if alien['color'] == 'Green':
        alien['color'] = 'Blue'
        alien['color'] = 'Orange'
        alien['color'] = 'Yellow'

for alien in aliens[0:3]:
      print(alien)
