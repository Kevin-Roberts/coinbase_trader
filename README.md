coinbase_trader
===============

A python application to set complex Coinbase trading orders. 
Market orders, Limits, stop losses, and trailing stop losses by percent and value.
Uses Coinbase API and your api_key or oauth2 credentials (https://coinbase.com/docs/api/authentication)
to execute real trades through Coinbase. Nearly every Coinbase API function has been implemented so you can
also send, receive, and request bitcoins or check your account information, transaction history, ect. 

Requirements
============

- coinbase_python library and its requirements (https://github.com/sibblegp/coinbase_python)


Example
=======

```python
from trader import Trader, CoinOrder
# oauth2 example setup can be seen in example.py of coinbase_python library
myTrader = Trader(api_key = 'my API key', logname = "mylog.txt")
# Setup order to Sell 0.5 bitcoin 10% lower than highest price seen by Trader.trade() 
# Use the optional price attribute to specify the max seen price so far, default is 0.
myTrader.setTrailingStopLossPercent(qty = 0.5, changeval = 10) 
# Setup order to Buy 0.5 bitcoin at 800 dollars per coin
myTrader.setLimitBuy(qty = 0.5, price = 800)
# Attempt to execute all trades once per sleep time until all trades have been executed
myTrader.trade(sleeptime = 60)
```


Notes
=====

- Can call functions from coinbase_python api via Trader.account object
- Occasionally receive "No JSON Object could be decoded" errors from Requests library. 
  TODO: try/except and retry once to see if that alleviates the problem.
- TODO: preserve orderbook in a file and optionally reload the orderbook via an input to the python call
        this would be more useful once the threading feature above were added to save the user input
        and the other reason for this is to save the max seen value for trailing stop loss orders.
        The only time that max value is lost when the CoinOrder object is destroyed for any reason. 
- TODO: Setup as module with setup.py vs just importing



Contributing / Credits
============
So far just me Kevin-Roberts but contributions are greatly appreciated.

Disclaimer
==========

This program executes REAL bitcoin trades with money from your coinbase account using the Coinbase API.
Use and trade with this program at your own risk as I am not liable for any losses incurred using this software.

License
=======

(The MIT License)

Copyright (c) 2013 Kevin Roberts <kr0b1486@hotmail.com>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the 'Software'), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
