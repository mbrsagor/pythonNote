"""
name = input("Enter your name: ")
color = input("Enter your favourite color: ")

print(f"{name} likes {color}")

birth_day = int(input("Enter your birthday? "))
current_date = 2019 - birth_day
print(current_date)

address = 'House #96 Road#19 "samsu" and Dhaka-1208'
print(address)


about_me = '''I am Sagor.
Come form Gaibandha.
Software developer.
'''
print(about_me)


p = "Python popular web framework is Django "
print(p[0: 3])
_p = p.split()
print(_p)



N = int(input())
if N % 2 == 0:
    print("Odd")
elif N:
    print("odd")
else:
    print("Event")

def recursion(_number):
    print(_number)
    _number += 1
    recursion(_number)


recursion(1)

"""


def func_ars(*args):
    print(f"{args} they are brother.")


func_ars('sagor', 'ohi', 'and shanto')


def calculator(**kwargs):
    temp = 0
    for key in kwargs:
        temp = temp + kwargs[key]
    print(f"tempTotal result: {temp}")


calculator(x=10, y=20, z=30)


def demo(**kwargs):
    print(f"My Info {kwargs}")


demo(name='mbr-sagor', email='mbrsagor@gmail.com', phone='+8801773474709')


def fabonic(num):
    if num == 0:
        return 1
    else:
        return num * fabonic(num - 1)


print(f"Total result: {fabonic(5)}")
