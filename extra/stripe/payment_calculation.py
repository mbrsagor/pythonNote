class AmountConverter(object):
    @staticmethod
    def to_real_amount(cents):
        return cents / 100

    @staticmethod
    def to_cents(amount):
        return int(amount * 100)


# Example usage
converter = AmountConverter()

real_amount = converter.to_real_amount(55070)
print(f"The real amount is: {real_amount:.2f}")  # Output: The real amount is: 550.70

cents = converter.to_cents(550.70)
print(f"The amount in cents is: {cents}")  # Output: The amount in cents is: 55070
