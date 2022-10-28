from models.address import Address

from repository.user_repository import find_user_by_email
from repository.address_repository import (
    create_new_address_on_bd,
    find_user_addresses_on_bd,
    find_address_by_id_on_bd,
    remove_user_addresses_on_bd,
    remove_address_by_id_on_bd,
    update_address_by_id_on_bd,
)


async def create_new_address(user_email: str, address: Address):
    if not await find_user_by_email(user_email):
        return "Theres no user registered with the given e-mail."
    if await find_address_by_id_on_bd(user_email, address.id):
        return "The address ID informed is already being used."
    address_dict = address.dict()
    if await create_new_address_on_bd(user_email, address_dict):
        return "Address registered sucessfully."


async def find_user_addresses(user_email: str):
    if not await find_user_by_email(user_email):
        return "Theres no user registered with the given e-mail."
    addresses = await find_user_addresses_on_bd(user_email)
    if addresses:
        return addresses
    return "This user doesnt have any address registered."


async def find_address_by_id(user_email: str, address_id: str):
    if not await find_user_by_email(user_email):
        return "Theres no user registered with the given e-mail."
    return await find_address_by_id_on_bd(user_email, address_id)


async def remove_user_addresses(user_email: str):
    if await find_user_by_email(user_email):
        if await remove_user_addresses_on_bd(user_email):
            return "User addresses excluded sucessfully."
    return "Theres no user registered with the given e-mail."


async def remove_address_by_id(user_email: str, address_id: str):
    if await find_user_by_email(user_email):
        if await find_address_by_id(user_email, address_id):
            if await remove_address_by_id_on_bd(user_email, address_id):
                return "Address excluded sucessfully."
        return "Theres no address registered with the given ID."
    return "Theres no user registered with the given e-mail."


async def update_address_by_id(
    user_email: str, address_id: str, updated_address: Address
):
    if await find_user_by_email(user_email):
        if address_id != updated_address.id:
            return "Address ID must remain the same."
        address_dict = updated_address.dict()
        await update_address_by_id_on_bd(user_email, address_id, address_dict)
        return "Address updated sucessfully."
    return "Theres no user registered with the given e-mail."
