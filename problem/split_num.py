# Prepare complementary ticket
def prepare_complementary_ticket(range_strings):
    # Initialize an empty list to store the individual integers
    integer_list = []
    # Iterate over each range string
    for range_str in range_strings:
        # Split each range string into start and end values
        start, end = map(int, range_str.split("-"))
        # Use range() to generate the integers and extend the integer_list
        integer_list.extend(list(range(start, end + 1)))
    return integer_list


ranges = ["191-250", "100-190", "1-99"]
ticket = prepare_complementary_ticket(ranges)
print(ticket)

