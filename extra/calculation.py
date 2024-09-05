def transaction_calculate(amount):
    percentage_others = 15
    percentage_donation = 10
    # Deduction
    deduction = (amount * percentage_others) / 100

    # Fee deduction
    fee_deduction = 0.75

    # Net payout
    net_payout = amount - deduction - fee_deduction

    # Admin payout
    admin_payout = amount - net_payout

    return {
        'deduction': deduction,
        'fee_deduction': fee_deduction,
        'net_payout': net_payout,
        'admin_payout': admin_payout
        }


result = transaction_calculate(180)
print(result)

