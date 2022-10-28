from models.user import User
from repository.user_repository import (
    insert_new_user,
    find_user_by_email,
    remove_user_by_email,
    update_user,
)


async def insert_user(new_user: User):
    if "@" not in new_user.email or len(new_user.email) < 4:
        return "E-mail inválido"
    if (new_user.email != new_user.shopping_cart.user_email) or (
        new_user.email != new_user.transaction_history.user_email
    ):
        return (
            "E-mail must be the same for user, shopping cart and transaction history."
        )
    if await find_user_by_email(new_user.email):
        return "The giver e-mail is already being used."
    new_user_dict = new_user.dict()
    await insert_new_user(new_user_dict)
    return "User registered seuccessfully."


async def get_user_email(email: str):
    found_user_dict = await find_user_by_email(email)
    if found_user_dict:
        return found_user_dict
    return "Theres no user registered with the given e-mail."


async def delete_user_by_email(email: str):
    if await find_user_by_email(email):
        if await remove_user_by_email(email):
            return "User excluded successfully."
        return "Error"
    return "Theres no user registered with the given e-mail."


async def update_user_by_email(email: str, features: dict):
    if await find_user_by_email(email):
        if await update_user(email, features):
            return "User updated successfully."
        return "Error"
    return "Theres no user registered with the given e-mail."
