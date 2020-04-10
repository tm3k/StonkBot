import creds
import finta
import alpaca_trade_api as tradeapi
import spx500
import pandas as pd

# Creates API object
api = tradeapi.REST(creds.api_key, creds.api_secret, api_version='v1') 

# Can only call 100 stocks at a time thru the api so had to split it up
set1 = spx500.spx[:100]
set2 = spx500.spx[101:201]
set3 = spx500.spx[202:302]
set4 = spx500.spx[303:403]
set5 = spx500.spx[404:504]
barsets1 = api.get_barset(set1, timeframe = '1D', limit = 30)
barsets2 = api.get_barset(set1, timeframe = '1D', limit = 30)
barsets3 = api.get_barset(set1, timeframe = '1D', limit = 30)
barsets4 = api.get_barset(set1, timeframe = '1D', limit = 30)
barsets5 = api.get_barset(set1, timeframe = '1D', limit = 30)


# Method for getting ohlc data for the stock and day specified
def get_ohlc_data(stock,day):
    day_open = stock[day].o
    day_high = stock[day].h 
    day_low = stock[day].l 
    day_close = stock[day].c 

    print(day_open)
    print(day_high)
    print(day_low)
    print(day_close)

# Test code for calling get_ohlc_data and getting the first(of 30) day's ohlc data
aapl_bars=barsets1['AAPL']
get_ohlc_data(aapl_bars,0)

# Method for passing each individual stock into get_ohlc_method through using a loop



# Method for taking stock ohlc data and creating pandas database


