from models.product import Product
from repository.product_repository import (
    insert_new_product,
    find_product_by_id_on_bd,
    find_product_by_name_on_bd,
    remove_product_by_id,
    update_product_by_id_on_bd,
)


async def create_new_product(new_product: Product):
    if await find_product_by_id_on_bd(new_product.id):
        return "The given product ID is already being used."
    product_dict = new_product.dict()
    await insert_new_product(product_dict)
    return "Product registered successfully."


async def find_product_by_id(product_id: str):
    product = await find_product_by_id_on_bd(product_id)
    if product:
        return product
    return "Theres no product registered with the given ID."


async def find_product_by_name(product_name):
    products = await find_product_by_name_on_bd(product_name)
    if products:
        return products
    return "No matches found."


async def delete_product_by_id(product_id: str):
    if await find_product_by_id_on_bd(product_id):
        if await remove_product_by_id(product_id):
            return "Product excluded successfully."
        return "Error"
    return "Theres no product registered with the given ID."


async def update_product_by_id(product_id: str, fields: dict):
    product = await find_product_by_id_on_bd(product_id)
    if product:
        if "id" in fields:
            return "Product ID cant be modified."
        if await update_product_by_id_on_bd(product_id, fields):
            return "Product updated successfully."
        print(product)
        return "Error"
    return "Theres no product registered with the given ID."
