from models.cart_product import CartProduct
from repository.shopping_cart_repository import (
    add_product_to_cart_on_bd,
    find_product_on_cart_on_bd,
    find_cart_products_on_bd,
    find_cart_on_bd,
    remove_product_from_cart_on_bd,
    clear_cart_on_bd,
    update_product_on_cart_on_bd,
    update_address_on_cart_on_bd,
)
from repository.purchase_repository import create_new_purchase_on_bd
from repository.user_repository import find_user_by_email
from repository.product_repository import find_product_by_id_on_bd
from repository.purchase_repository import find_purchase_by_id_on_bd
from repository.address_repository import find_address_by_id_on_bd


async def add_product_to_cart(user_email: str, cart_product: CartProduct):
    if await find_user_by_email(user_email):
        if await find_product_by_id_on_bd(cart_product.product_id):
            if cart_product.quantity < 0:
                return "The quantity informed must be a positive integer."
            cart_product.quantity = int(cart_product.quantity)
            cart_product_dict = cart_product.dict()
            if await add_product_to_cart_on_bd(user_email, cart_product_dict):
                return "Products added to cart successfully."
            return "Error"
        return "Theres no product registered with the given ID."
    return "Theres no user registered with the given e-mail."


async def cart_to_purchase(user_email: str, purchase_id: str, payment_method: str):
    user_cart = await find_cart_on_bd(user_email)
    products_list = user_cart["products"]
    if not products_list:
        return "Theres no item on cart."
    if await find_purchase_by_id_on_bd(user_email, purchase_id):
        return "The given ID is already being used."
    if payment_method == "credit":
        price = user_cart["price_credit"]
    elif payment_method == "debit":
        price = user_cart["price_debit"]
    else:
        return "Payment method must be 'credit' or 'debit'."

    purchase = {}
    purchase["id"] = purchase_id
    purchase["products"] = products_list
    purchase["price"] = price
    purchase["number_of_items"] = user_cart["number_of_items"]
    purchase["delivery_address"] = user_cart["delivery_address"]
    purchase["payment_method"] = payment_method
    await clear_cart_on_bd(user_email)
    if await create_new_purchase_on_bd(user_email, purchase):
        return "Purchase registered sucessfully."
    return "Error"


async def find_product_on_cart(user_email: str, product_id: str):
    if await find_user_by_email(user_email):
        if await find_product_by_id_on_bd(product_id):
            product_found = await find_product_on_cart_on_bd(user_email, product_id)
            if product_found:
                return product_found
            return "Error"
        return "Theres no product registered with the given ID."
    return "Theres no user registered with the given e-mail."


async def find_cart_products(user_email: str):
    if await find_user_by_email(user_email):
        product_list = await find_cart_products_on_bd(user_email)
        if product_list:
            return product_list
        return "Empty shopping cart."
    return "Theres no user registered with the given e-mail."


async def find_cart(user_email: str):
    if await find_user_by_email(user_email):
        return await find_cart_on_bd(user_email)
    return "Theres no user registered with the given e-mail."


async def remove_product_from_cart(user_email: str, product_id: str):
    if await find_user_by_email(user_email):
        if await find_product_by_id_on_bd(product_id):
            if await remove_product_from_cart_on_bd(user_email, product_id):
                return "All products from the given ID have been removed."
            return "Error"
        return "Theres no product registered with the given ID."
    return "Theres no user registered with the given e-mail."


async def clear_cart(user_email: str):
    if await find_user_by_email(user_email):
        if await clear_cart_on_bd(user_email):
            return "All data from cart has been reseted."
    return "Theres no user registered with the given e-mail."


async def update_product_on_cart(user_email: str, cart_product: CartProduct):
    if await find_user_by_email(user_email):
        if await find_product_by_id_on_bd(cart_product.product_id):
            cart_product_dict = cart_product.dict()
            if await update_product_on_cart_on_bd(user_email, cart_product_dict):
                return "Products updated on cart successfully."
            return "Error"
        return "Theres no product registered with the given ID."
    return "Theres no user registered with the given e-mail."


async def update_address_on_cart(user_email: str, address_id: str):
    if await find_user_by_email(user_email):
        address = await find_address_by_id_on_bd(user_email, address_id)
        if address:
            if await update_address_on_cart_on_bd(user_email, address):
                return "Address updated sucessfully."
            return "Error"
        return "Theres no address registered with the given ID."
    return "Theres no user registered with the given e-mail."
