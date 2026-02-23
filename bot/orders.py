from bot.validators import *
import logging

class OrderService:
    def __init__(self, client):
        self.client = client
        self.logger = logging.getLogger()

    def execute_order(self, symbol, side, order_type, quantity, price=None):

        validate_side(side)
        validate_order_type(order_type)
        validate_quantity(quantity)
        validate_price(price, order_type)

        params = {
            "symbol": symbol.upper(),
            "side": side,
            "type": order_type,
            "quantity": quantity
        }

        if order_type == "LIMIT":
            params["price"] = price
            params["timeInForce"] = "GTC"

        return self.client.place_order(**params)