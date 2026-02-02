import argparse
import logging
from bot.client import BinanceFuturesClient
from bot.orders import place_trade
from bot.logging_config import setup_logging
from dotenv import load_dotenv
import os
load_dotenv()

API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_API_SECRET")

def main():
    setup_logging()

    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True, choices=["BUY", "SELL"])
    parser.add_argument("--type", required=True, choices=["MARKET", "LIMIT"])
    parser.add_argument("--quantity", required=True, type=float)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    try:
        client = BinanceFuturesClient(API_KEY, API_SECRET)

        print("\n📌 Order Request Summary")
        print(vars(args))

        response = place_trade(
            client=client,
            symbol=args.symbol,
            side=args.side,
            order_type=args.type,
            quantity=args.quantity,
            price=args.price
        )

        print(f"Order ID: {response.get('orderId')}")
        print(f"Status: {response.get('status')}")
        print(f"Executed Qty: {response.get('executedQty')}")
        print(f"Avg Price: {response.get('avgPrice')}")

    except Exception as e:
        logging.error(str(e))
        print("\n❌ Order Failed")
        print(str(e))

if __name__ == "__main__":
    main()
