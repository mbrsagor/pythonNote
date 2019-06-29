class Section1(object):

    def __init__(self):
        print("I am calling from super class")

    def common_option(self):
        print("I am calling from common option")

    def new_option(self):
        print("Hello everybody, I am calling from new option")


class Section2(Section1):

    def common_option(self):
        print("Here updated common option some text")


class Section3(object):

    def say_hello(self):
        print("I am section three class")


class LastClass(Section2, Section3):

    def __init__(self):
        super().__init__()
        print("I am calling from sub class")

    def new_option(self):
        print("Last class new option from here")

    def say_hello(self):
        print("I am saying from Last class.")
        super(LastClass, self).say_hello()


last = LastClass()
last.new_option()
last.say_hello()
