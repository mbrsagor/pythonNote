def add(x, y):
    z = x + y
    return z


print(add(20, 30))

print('\n')

def say_hello(name):
    print("Hello", name)


say_hello("sagor")
print('\n')

def multiplay(*numbers):
    for number in numbers:
        print(number)


multiplay(6, 87, 90, 66)
print('\n')

def saveUser(**kwargs):
    print(kwargs)


saveUser(username="sagor", password=12345)
