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
    print (obj.get_account_info())

    # Example. Refer to https://docs.ftx.com/?python#place-order
    # obj.place_order(
    #   market="BTC-PERP",
    #   side="sell",
    #   price=100000,
    #   type="limit",
    #   size=1,
    #   reduce_only=False,
    #   ioc=False,
    #   post_only=False,
    #   client_id=None,
    # )
