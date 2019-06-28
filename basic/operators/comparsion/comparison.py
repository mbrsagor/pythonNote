temperature = 25

if temperature >= 28:
    if temperature == 25:
        message = "Nice weather.. Enjoy the day."
    else:
        message = "Every hot weather... :("
else:
    message = "very cool weather"

print(message)

# ternary operator using same like this
"""
message = "Nice weather... Enjoy the day" if temperature >= 28 else "Very hot weather this moment"
print(message)
"""
