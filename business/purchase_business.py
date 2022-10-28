from models.purchase import Purchase
from repository.purchase_repository import (
    create_new_purchase_on_bd,
    find_purchase_by_id_on_bd,
    find_transaction_history_on_bd,
)
from repository.user_repository import find_user_by_email


async def create_new_purchase(user_email: str, purchase: Purchase):
    if await find_user_by_email(user_email):
        if await find_purchase_by_id_on_bd(user_email, purchase.id):
            return "The given purchase ID is already being used."
        purchase_dict = purchase.dict()
        if await create_new_purchase_on_bd(user_email, purchase_dict):
            return "Purchase registered sucessfully."
        return "Error"
    return "Theres no user registered with the given e-mail."


async def find_purchase_by_id(user_email: str, purchase_id: str):
    if await find_user_by_email(user_email):
        purchase = await find_purchase_by_id_on_bd(user_email, purchase_id)
        if purchase:
            return purchase
        return "No purhcase registered with the given ID."
    return "Theres no user registered with the given e-mail."


async def find_transaction_history(user_email: str):
    if await find_user_by_email(user_email):
        transaction_history = await find_transaction_history_on_bd(user_email)
        if transaction_history["transaction_history"]:
            return transaction_history
        return "This user doesnt have a transaction history."
    return "Theres no user registered with the given e-mail."
