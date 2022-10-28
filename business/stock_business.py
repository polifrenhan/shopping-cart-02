from repository.product_repository import find_product_by_id_on_bd
from repository.stock_repository import (
    get_stock_on_bd,
    update_product_quantity_on_bd,
    update_stock_on_bd,
)


async def update_product_quantity(product_id: str, sum: dict):
    sum["stock"] = int(sum["stock"])
    product = await find_product_by_id_on_bd(product_id)
    stock = await get_stock_on_bd(product_id)
    stock_stock = stock["stock"]
    quantity = stock_stock + sum["stock"]
    if quantity >= 0:
        if product:
            await update_product_quantity_on_bd(product_id, sum)
            return "Stock updated successfully."
        return "Theres no product registered with the given ID."
    sum_stock = abs(sum["stock"])
    return f"Youre trying to buy {sum_stock} products {product_id}. There is/are only {stock_stock} available on stock."


async def update_stock(product_id: str, quantity: dict):
    quantity["stock"] = int(quantity["stock"])
    if await find_product_by_id_on_bd(product_id):
        if quantity["stock"] < 0:
            return "Stock can't have negative entrance."
        await update_stock_on_bd(product_id, quantity)
        return "Stock updated successfully."
    return "Theres no product registered with the given ID."
