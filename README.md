# FTX Sample Code

[FTX](https://ftx.com/) is a cryptocurrency derivatives exchange.

You can find the REST API docs [here](https://ftx1.docs.apiary.io), websocket API docs [here](https://ftxwebsocket.docs.apiary.io), and FIX docs [here](https://docs.ftx.com/#fix-api).

You can create API keys on your [profile page](https://ftx.com/profile).

FTX is integrated with CCXT here:
- https://github.com/ccxt/ccxt/blob/master/js/ftx.js
- https://github.com/ccxt/ccxt/blob/master/python/ccxt/ftx.py
- https://github.com/ccxt/ccxt/blob/master/python/ccxt/async_support/ftx.py
- https://github.com/ccxt/ccxt/blob/master/php/ftx.php

## Interact with FTX account

### Obtain credentials


* Go to https://ftx.com/profile, and in the "API Keys" section choose to "Create a Read-Only API Key".
* Record the API Key and API Secret that it provides
* Record the name of the Subaccount that you've used to setup the API credentials.

### macOS

Fork and clone https://github.com/ftexchange/ftx:
```
git clone git@github.com:ltfschoen/ftx.git
cd rest
```

Install Python 3
```
brew install python3
pip3 install --upgrade pip setuptools
```

Create a .env file based on the example to contain your credentials
```
cp .env-example .env
```

Add your credentials values to the .env file to correspond with each key.

Install Python dependencies
```
pip3 install -r requirements.txt
```

Run your custom script to call the  `get_account_info` function in /rest/client.py that will authenticae you and return your account info
```
cd rest/
python3 main.py
```

Add additional functionality to your script by updating /rest/main.py to otherwise interact with the FTX REST API https://docs.ftx.com/#rest-api. For example, if you've been trading as a "Machine" and have positions that are open through you creating and enabling different trading strategy rules in the Quant Zone https://ftx.com/quant-zone/rules, then to close one of your trades you'll have to place an order to close part or all of your position using the FTX REST API https://docs.ftx.com/?python#place-order, and call the `place_order` function in /rest/client.py. An example of a function call has been included in that file.

The content provided in this repository is for informational purposes only, you should not construe any such information or other material as legal, tax, investment, financial, or other advice.

Note: If you have a `Short` position, and you try to make a `Long` position of the same size to cancel the trade but you get error `Exception: Account does not have enough margin for order.`, then it may be because you have some open orders that you should first cancel with `cancel_orders` or similar.