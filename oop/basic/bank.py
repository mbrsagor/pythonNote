class MyBank(object):

    def __init__(self):
        print("Welcome to our new bank\n=====================\n")
        self.balance = 0

    def deposit(self, amount):
        """deposit amount form here"""
        self.balance += amount
        print(f"Deposit amount: {self.balance}")

    def withDraw(self, amount):
        """how many balance withdraw amount from here"""
        if self.balance > 0:
            self.balance -= amount
            print(f"With draw amount: {amount}")
        else:
            print("sorry !! low balance")

    def checkBalance(self):
        """check account balance"""
        print(f"Total balance: {self.balance}")


if __name__ == '__main__':
    """
    Here instantiating `MyBank` class
    """

    my_bank = MyBank()
    my_bank.deposit(250)
    my_bank.withDraw(50)
    my_bank.checkBalance()
    my_bank.withDraw(200)
    my_bank.withDraw(100)
    my_bank.deposit(2500)
    my_bank.checkBalance()
