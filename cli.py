import argparse
import os
from dotenv import load_dotenv
from bot.client import BinanceSpotClient
from bot.orders import OrderService
from bot.logging_config import setup_logger

def main():
    setup_logger()
    load_dotenv()

    parser = argparse.ArgumentParser(description="Binance Spot Testnet Trading Bot")

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", type=float, required=True)
    parser.add_argument("--price", type=float)

    args = parser.parse_args()

    api_key = os.getenv("API_KEY")
    api_secret = os.getenv("API_SECRET")

    client = BinanceSpotClient(api_key, api_secret)
    order_service = OrderService(client)

    try:
        print("\n===== ORDER SUMMARY =====")
        print(f"Symbol: {args.symbol}")
        print(f"Side: {args.side}")
        print(f"Type: {args.type}")
        print(f"Quantity: {args.quantity}")
        if args.price:
            print(f"Price: {args.price}")

        response = order_service.execute_order(
            symbol=args.symbol,
            side=args.side,
            order_type=args.type,
            quantity=args.quantity,
            price=args.price
        )

        print("\n===== ORDER RESPONSE =====")
        print(f"Order ID: {response['orderId']}")
        print(f"Status: {response['status']}")
        print(f"Executed Qty: {response.get('executedQty')}")

        print("\n✅ Order Successful!")

    except Exception as e:
        print(f"\n❌ Order Failed: {e}")

if __name__ == "__main__":
    main()