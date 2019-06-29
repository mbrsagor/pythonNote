class Laptop(object):
    # class variable
    backup = "3-4 hours"

    def __init__(self):
        self.name = "Laptop"
        self.brand = "Lenovo"
        self.color = "Black"
        self.price = 120000


laptop = Laptop()
print(laptop.name, laptop.brand, laptop.color, laptop.price, f"Total charge backup: {laptop.backup}")

print(Laptop.backup)
