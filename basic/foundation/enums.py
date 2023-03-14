from enum import Enum
from dataclasses import dataclass

class MyOrder(str, Enum):
    PLACED = "PLACED"
    CANCELED = "CANCELED"
    ACCEPTED = "ACCEPTED"


@dataclass
class Order:
    status: MyOrder



order = Order(MyOrder.PLACED)
print(order)
