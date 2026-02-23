from binance.client import Client
from binance.exceptions import BinanceAPIException
import logging

class BinanceSpotClient:
    def __init__(self, api_key, api_secret):
        self.client = Client(api_key, api_secret, testnet=True)
        self.logger = logging.getLogger()

    def place_order(self, **params):
        try:
            self.logger.info(f"Order Request: {params}")
            response = self.client.create_order(**params)
            self.logger.info(f"Order Response: {response}")
            return response
        except BinanceAPIException as e:
            self.logger.error(f"Binance API Error: {e}")
            raise
        except Exception as e:
            self.logger.error(f"Unexpected Error: {e}")
            raise