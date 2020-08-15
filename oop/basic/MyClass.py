class A(object):

    def __init__(self):
        print("Super class init")

    def featurel1(self):
        print("This is first class")

    def featurel2(self):
        print("This is second class")


class B(object):

    def __init__(self):
        print("Sub class init")

    def something(self):
        print("I do something")


class C(A, B):

    def __init__(self):
        super(C, self).__init__()
        super(A, self).__init__()
        print("Last class init")

    def getMethod(self):
        print("it's worked!!")
        super().featurel1(),super().featurel2()


c1 = C()
c1.getMethod()
