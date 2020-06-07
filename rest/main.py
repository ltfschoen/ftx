from dotenv import load_dotenv
from pathlib import Path  # python3 only
env_path = Path('../') / '.env'
load_dotenv(dotenv_path=env_path, verbose=True)

import sys
import os # for dotenv

import client

if __name__ == '__main__':
    API_KEY = os.getenv("API_KEY")
    API_SECRET = os.getenv("API_SECRET")
    SUBACCOUNT_NAME = os.getenv("SUBACCOUNT_NAME")

    obj = client.FtxClient(API_KEY, API_SECRET, SUBACCOUNT_NAME)
    # Refer to FTX REST API Docs https://docs.ftx.com/?python#account
    # print (obj.get_account_info())
    # print (obj.get_positions())

    # obj.get_order_history(
    #   market="FTT/USD",
    # )

    # obj.cancel_orders(
    #   market_name="SHIT-PERP",
    # )

    # Example. Refer to https://docs.ftx.com/?python#place-order
    obj.place_order(
      market="SHIT-PERP",
      side="buy",
      price=890,
      type="limit",
      size=0.01,
      reduce_only=False,
      ioc=False,
      post_only=False,
      client_id=None,
    )

    # Refer to https://docs.ftx.com/?python#place-trigger-order
    obj.place_conditional_order(
      market="SHIT-PERP",
      side="sell",
      trigger_price=889.1, # to send a stop market order
      type="stop",
      # limit_price=889.1, # to send a stop limit order, instead of market order
      size=0.01,
      reduce_only=False,
      cancel=False, # cancel limit on trigger
      trail_value=None, 
    )

    obj.place_conditional_order(
      market="SHIT-PERP",
      side="sell",
      trigger_price=891.1,
      type="take_profit",
      limit_price=891.1,
      size=0.01,
      reduce_only=False,
      cancel=False,
      trail_value=None, 
    )
