from pydantic import BaseModel
from typing import List, Dict

from models.cart_product import CartProduct


class ShoppingCart(BaseModel):
    user_email: str
    products: List[CartProduct] = []
    price_credit: float = 0.0
    price_debit: float = 0.0
    number_of_items: int = 0
    delivery_address: Dict = {}
