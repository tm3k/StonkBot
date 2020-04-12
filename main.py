import creds
from finta import TA
import alpaca_trade_api as tradeapi
import spx500
import pandas as pd
import numpy as np

# Creates API object
api = tradeapi.REST(creds.api_key, creds.api_secret, api_version='v1') 


# Can only call 100 stocks at a time thru the api so had to split it up
set1 = spx500.spx[:100]
set2 = spx500.spx[101:201]
set3 = spx500.spx[202:302]
set4 = spx500.spx[303:403]
set5 = spx500.spx[404:504]
barsets1 = api.get_barset(set1, timeframe = '1D', limit = 60)
barsets2 = api.get_barset(set1, timeframe = '1D', limit = 60)
barsets3 = api.get_barset(set1, timeframe = '1D', limit = 60)
barsets4 = api.get_barset(set1, timeframe = '1D', limit = 60)
barsets5 = api.get_barset(set1, timeframe = '1D', limit = 60)



# Method for getting ohlc data for the stock 30 days at a time
def prep_data(stock):
    open_vals = []
    for i in stock:
        day_open = i.o
        open_vals.append(day_open)

    high_vals = []
    for i in stock:
        day_high = i.h
        high_vals.append(day_high)

    low_vals = []
    for i in stock:
        day_low = i.l
        low_vals.append(day_low)

    close_vals = []
    for i in stock:
        day_close = i.c
        close_vals.append(day_close)


    candle_times = []
    for i in stock:
        candle_time = i.t 
        candle_times.append(candle_time)


    zippedList = list(zip(open_vals, high_vals, low_vals, close_vals))
    df = pd.DataFrame(zippedList, columns = ['open' , 'high', 'low', 'close'])
    df['time'] = candle_times

    # Magic code to remove hours minutes and seconds from timestamp, formats code for viewing
    df['time'] = pd.to_datetime(df['time'])
    df['time'] = df['time'].dt.date
    
    bb = TA.PERCENT_B(df)
    bb = np.nan_to_num(bb)
    df["%BB"] = bb
    

    trade_signal = []
    for i in bb:
        
        if i == 0:
            trade_signal.append(''),
        elif i > 1:
            trade_signal.append('X'),
        elif i < 0:
            trade_signal.append('X'),
        elif i <= 1 and i >= 0:
            trade_signal.append('')

    action = pd.DataFrame(trade_signal)
    df['Trade'] = action

    pd.set_option('display.width', None)
    pd.set_option('display.max_rows', 60)
    return df
    


    


# Test code for calling get_ohlc_data and getting the first(of 30) day's ohlc data
aapl_bars=barsets1['AAPL']
AAPL = prep_data(aapl_bars)

print(AAPL)






