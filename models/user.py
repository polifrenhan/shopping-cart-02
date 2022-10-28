from typing import List
from pydantic import BaseModel

from models.address import Address
from models.shopping_cart import ShoppingCart
from models.transaction_history import TransactionHistory


class User(BaseModel):
    name: str
    email: str
    password: str
    addresses: List[Address] = []
    shopping_cart: ShoppingCart
    transaction_history: TransactionHistory
