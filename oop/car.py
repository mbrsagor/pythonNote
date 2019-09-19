class Human(object):
    data = "20-December-2014"

    def __init__(self, man, woman):
        self.man = man
        self.woman = woman
        self._person = self.Person()

    def population(self):
        print(f"He is a {self.man}\nShe is a {self.woman}\nThey talk to {self.data}")

    @classmethod
    def remember(cls):
        print(cls.data)

    @staticmethod
    def charter():
        print("He and she is very good man.")

    class Person(object):
        def __init__(self):
            self.hand = 2
            self.eye = 2
            self.color = "White"

        def about_me(self):
            print(f"I have {self.hand} hand, {self.eye} eye and my color is {self.color}.")


hum1 = Human("Sagor", "Ritu")
hum1.population()

hum2 = Human("Zia", "Mithu")
hum2.population()

Human.data = "14 April 2019"
Human.man = "Novel"

print("\n=============")

Human.remember()
Human.charter()

hum2._person.about_me()
