from enum import Enum, unique

@unique
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
    # If you try to add another member with the same value, it will raise a ValueError
    # e.g., YELLOW = 1 would cause an error

