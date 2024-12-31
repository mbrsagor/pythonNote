from datetime import datetime


def calculate_age(birth_date):
    today = datetime.today()
    age = today.year - birth_date.year
    # Adjust for the case where the birthday hasn't occurred yet this year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1
    return age

# Example usage
birth_date = datetime(1990, 5, 25)  # Replace with the actual date of birth
age = calculate_age(birth_date)
print(f"Age: {age}")

