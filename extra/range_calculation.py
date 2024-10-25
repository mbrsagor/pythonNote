def calculate_payable_amount(ticket_count: int) -> float:
    total_amount = 0.0

    price_ranges = [(250, 2.50), (500, 2.35), (1000, 2.25)]
    last_range_price = 2.15

    # [{'qnt': '1000,10000', 'price': Decimal('2.15')}, {'qnt': '501,1000', 'price': Decimal('2.25')}, {'qnt': '251,500', 'price': Decimal('2.35')}, {'qnt': '1,250', 'price': Decimal('2.50')}]

    remaining_tickets = ticket_count

    for range_value, price in price_ranges:
        if remaining_tickets > 0:
            tickets_for_range = (
                range_value if remaining_tickets >= range_value else remaining_tickets
            )
            total_amount += tickets_for_range * price
            remaining_tickets -= tickets_for_range

    if remaining_tickets > 0:
        total_amount += remaining_tickets * last_range_price

    return total_amount


if __name__ == "__main__":
    ticket_count = 270
    total_amount = calculate_payable_amount(ticket_count)
    print(f"Payable amount for {ticket_count} tickets = ${total_amount:.2f}")

