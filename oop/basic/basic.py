class Car(object):
    price = 1200000

    def __init__(self):
        self.name = "BMW"
        self.color = "Red"
        self.new_car = self.NewCar()

    def getAll(self):
        return f"Car name: {self.name}\nCar color:{self.color}"

    @classmethod
    def car_price(cls):
        return f"Car price: {cls.price}"

    @staticmethod
    def something():
        x = 10
        y = 20
        z = x + y
        return f"Total Calculate price: {z}"

    def getInner_class(self):
        return self.NewCar()

    class NewCar(object):

        def __init__(self):
            self.brand = "New brand"
            self.CC = 1.6

        def get_car(self):
            return f"Car brand: {self.brand}\nEngin CC:{self.CC}"


car = Car()

print(car.getAll())

print(Car.car_price())

print(Car.something())

print(car.new_car.brand)

print(car.getInner_class().get_car())
