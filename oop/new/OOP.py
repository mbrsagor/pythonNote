class Vehicle(object):
    """  Main class, call name `super` class for all vehicle """

    def __init__(self, name, manufacturer, color):
        """ Initializing a  `constructor` form here   """
        self.name = name
        self.manufacturer = manufacturer
        self.color = color

    def drive(self):
        print("Drive on", self.manufacturer, self.name)

    def turn(self, direction):
        print("Turing", self.name, "to", direction)

    def brake(self):
        print(self.name, "is stop")

    @staticmethod
    # this method call name `static method`
    def mySelf():
        print("I am mbr-sagor.I can well be driving the car")

    @classmethod
    def engine_cc(cls, cc):
        try:
            print(f"Vehicle Name: {cls.name} and Engine CC: {cc}")
        except Exception as e:
            print(e)
        finally:
            print("sorry we could not find the name")

    @property
    def name_color(self):
        print(f"Name: {self.name} and Color: {self.color}")

    @classmethod
    def separator(cls):
        print("\n======================\n")


if __name__ == '__main__':
    vechile_instance1 = Vehicle("BMW", "Walton", "Red")
    vechile_instance1.drive()
    vechile_instance1.turn("Left")
    vechile_instance1.brake()
    vechile_instance1.name_color

    vechile_instance1.separator()


class Car(Vehicle):
    """ `Car` class, this class called subclass"""

    place_name = "Gaibandha"

    def __init__(self, name, manufacturer, color, year):
        """ Initializing a sub class `constructor` form here   """
        super(Car, self).__init__(name, manufacturer, color)
        self.name = name
        self.manufacturer = manufacturer
        self.color = color
        self.year = year
        self.wheels = 4

        print("A new car has been created. Name:", self.name)
        print("It has been:", self.wheels, "wheels")
        print(self.name, "has been created:", self.year)

    def change_gear(self, gear_name):
        """ this method using change gear """
        print(self.name, "is changing gear to", gear_name)

    def turn(self, direction):
        """
        Here overriding is the property of `Super` class
        :param direction: is a right side
        :return: place name
        """
        print("Turing", self.name, "to", direction, "at", self.place_name)

    def stop_car(self):
        """ Here call `super` class method"""
        super().brake()
        super().engine_cc("750")


if __name__ == '__main__':
    """
         Here after instantiating the `Car` class. And here access `Vehicle` class all method and variable
    """

    car_instance = Car("MyCar", "Walton", "Red", 2019)
    car_instance.drive()
    car_instance.change_gear("160Deg")
    car_instance.turn("right side")
    car_instance.stop_car()
    car_instance.mySelf()
