def calculate_total(quantity):
    # Pricing tiers
    price_tier_1 = 2.50  # 1 to 250 units
    price_tier_2 = 2.35  # 251 to 500 units
    price_tier_3 = 2.25  # 501 to 1000 units
    price_tier_4 = 2.15  # 1001+ units

    if quantity <= 250:
        total = quantity * price_tier_1
    elif quantity <= 500:
        total = (250 * price_tier_1) + ((quantity - 250) * price_tier_2)
    elif quantity <= 1000:
        total = (250 * price_tier_1) + (250 * price_tier_2) + ((quantity - 500) * price_tier_3)
    else:
        total = (250 * price_tier_1) + (250 * price_tier_2) + (500 * price_tier_3) + ((quantity - 1000) * price_tier_4)
    
    return total

# Example usage
quantity = 1010
total_price = calculate_total(quantity)
print(f"The total price for {quantity} items is: ${total_price:.2f}")

