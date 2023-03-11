import math as m

print(m.ceil(2.40))
print(m.floor(7.9))
print(m.copysign(50, 20))

x = 10
y = -5
z = m.copysign(x, y)
print(z)

print(m.fabs(-60.87))
print(m.fabs(21))

print(m.factorial(5))

print(m.fmod(56, 90))

abc = m.sqrt(25)
print(int(abc))

print(m.pi)
print(m.e)

print(m.sqrt(4))


def circle_area(r):
    return m.pi * r ** 2


radius = 3
print("Area =", circle_area(radius))
