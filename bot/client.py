from binance.client import Client
import logging

class BinanceFuturesClient:
    def __init__(self, api_key: str, api_secret: str):
        self.client = Client(api_key, api_secret, testnet=True)

        self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

    def place_order(self, **kwargs):
        logging.info(f"Order Request: {kwargs}")

        response = self.client.futures_create_order(**kwargs)

        logging.info(f"Order Response: {response}")
        return response
