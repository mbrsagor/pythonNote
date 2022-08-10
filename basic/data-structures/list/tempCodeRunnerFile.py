# radis = radians(5)
# print(radis)

brand = ["Lenovo", "HP", "Apple", "Samsung", "Asus", "Doyal", "Tosuba"]
print(brand)

sorted_brand = sorted(brand)
print(sorted_brand)

brand.sort()
print(brand)

# Here `.sort` and `sorted` are same work

ages = [5, 12, 17, 18, 24, 32]


def function(age):
    if age < 18:
        return False
    else:
        return True


adults = filter(function, ages)
print(adults)
for adult in adults:
    print(adult)


def apply_discount(product, discount):
    price = int(product['price'] * (1.0 - discount))
    assert 0 <= price <= product['price']
    return price


shoes = {'name': 'Fancy Shoes', 'price': 14900}
print(apply_discount(shoes, 0.25))
