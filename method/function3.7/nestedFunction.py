def myFunction():
    print("Hello, I am super function")

    def childFunction():
        print("I am child function")

    childFunction()

    def seperator():
        print('==================\n')

    seperator()


myFunction()


def nastedFunction(x,y):
    z = x + y
    print(f"Total Main: {z}")

    def childFunc(a,b):
        c = a + x
        print(f"Total sub: {c}")

    childFunc(40,10)


nastedFunction(10,20)
