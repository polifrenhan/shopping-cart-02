from bd import get_collection
from repository.user_repository import update_user

USERS_COLLECTION = get_collection("users")
TRANSACTION_HISTORY_COLLECTION = get_collection("transaction-history")


async def create_new_purchase_on_bd(user_email: str, purchase: dict):
    transaction_history = await find_transaction_history_on_bd(user_email)
    purchase_list = transaction_history["transaction_history"]
    purchase_list.append(purchase)
    check = await TRANSACTION_HISTORY_COLLECTION.update_one(
        {"user_email": user_email}, {"$set": {"transaction_history": purchase_list}}
    )
    await update_user(user_email, {"transaction_history": purchase_list})
    return check.modified_count == 1


async def find_purchase_by_id_on_bd(user_email: str, purchase_id: str):
    transaction_history = await find_transaction_history_on_bd(user_email)
    purchase_list = transaction_history["transaction_history"]
    for purchase in purchase_list:
        if purchase["id"] == purchase_id:
            return purchase
    return False


async def find_transaction_history_on_bd(user_email: str):
    return await TRANSACTION_HISTORY_COLLECTION.find_one(
        {"user_email": user_email}, {"_id": 0}
    )
