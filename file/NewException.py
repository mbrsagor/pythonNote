class ExceptionHandling(object):

    def addingNumber(self, a, b):
        c = a + b
        print(f"Total calculation number: {c}")

    def divitionNumber(self, a, b):
        try:
            c = a // b
            print(f"Total calculation number: {c}")
        except Exception as e:
            print(e)
        finally:
            print("Thank you!!")


exception1 = ExceptionHandling()
exception1.addingNumber(20, 0)
exception1.divitionNumber(50, 2)
