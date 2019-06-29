class Man(object):

    def __init__(self, name):
        print(f"I am calling from {name}")

    def speak(self):
        print("He speek bangal and english both")


man1 = Man('constructor')
man2 = Man('method')
man1.speak()
Man.speak(man2)

if man1 == man2:
    print("They are same.")
else:
    print("They are different.")

