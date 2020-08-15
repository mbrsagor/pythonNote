class Calculate(object):

    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    def increment(self):
        return f"Total calculate increment is: {self.number1 + self.number2}"

    def decrement(self):
        return f"Total calculate decrement is: {self.number1 - self.number2}"


class NewCalculator(Calculate):

    def multiplication(self):
        return f"Total calculate multiplication is: {self.number1 * self.number2}"


# instantiating new-calculate class
if __name__ == '__main__':
    calculator1 = NewCalculator(20, 10)
    print(calculator1.increment())
    print(calculator1.decrement())
    print(calculator1.multiplication())
