from fastapi import FastAPI

from controller.main_controller import MAIN_ROUTE
from controller.product_controller import PRODUCT_ROUTE
from controller.user_controller import USER_ROUTE
from controller.address_controller import ADDRESS_ROUTE
from controller.stock_controller import STOCK_ROUTE
from controller.shopping_cart_controller import SHOPPING_CART_ROUTE
from controller.purchase_controller import TRANSACTION_HISTORY_ROUTE


def route_config(app: FastAPI):
    app.include_router(MAIN_ROUTE)
    app.include_router(PRODUCT_ROUTE)
    app.include_router(USER_ROUTE)
    app.include_router(ADDRESS_ROUTE)
    app.include_router(STOCK_ROUTE)
    app.include_router(SHOPPING_CART_ROUTE)
    app.include_router(TRANSACTION_HISTORY_ROUTE)


def create_api():
    app = FastAPI()
    route_config(app)
    return app
