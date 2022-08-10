def is_event(number):
    if number % 2 == 0:
        return True
    else:
        return False


start_number = 0

while start_number < 100:
    if is_event(start_number):
        print(f"{start_number} is event")
    else:
        print(f"{start_number} is Odd")
    start_number = start_number + 1

print("The End")
