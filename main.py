import creds
from finta import TA
import alpaca_trade_api as tradeapi
import spx500
import pandas as pd
import numpy as np
import matplotlib as mpl
import time

# Creates API object
api = tradeapi.REST(creds.api_key, creds.api_secret, api_version='v1') 

# Can only call 100 stocks at a time thru the api so had to split it up
set1 = spx500.stocklist[:100]
set2 = spx500.stocklist[100:200]
set3 = spx500.stocklist[200:300]
set4 = spx500.stocklist[300:400]
set5 = spx500.stocklist[400:500]
set6 = spx500.stocklist[500:600]

barsets1 = api.get_barset(set1, timeframe = '1D', limit = 100)
barsets2 = api.get_barset(set2, timeframe = '1D', limit = 100)
barsets3 = api.get_barset(set3, timeframe = '1D', limit = 100)
barsets4 = api.get_barset(set4, timeframe = '1D', limit = 100)
barsets5 = api.get_barset(set5, timeframe = '1D', limit = 100)
barsets6 = api.get_barset(set6, timeframe = '1D', limit = 100)
# barsets7 = api.get_barset(set7, timeframe = '1D', limit = 100)


# Method for getting ohlc data for the stock 30 days at a time
def make_df(stock):
    
    #Puts all ohlc data into lists
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
    
    # %B indicator added to df
    bb = TA.PERCENT_B(df)
    bb = np.nan_to_num(bb)  #replaces NaN values with 0.0
    df["%BB"] = bb #Adds %b value column to df
    trade_signal = [] #loops thru %b values
    for i in bb:
        
        if i == 0:
            trade_signal.append(''),
        elif i > 1:
            trade_signal.append('XXXXXXX'),
        elif i < 0:
            trade_signal.append('XXXXXXX'),
        elif i <= 1 and i >= 0:
            trade_signal.append('')

    #Adds trade column to df
    action = pd.DataFrame(trade_signal)
    df['Trade'] = action

    #For viewer ease of use
    pd.set_option('display.width', None)
    pd.set_option('display.max_rows', None)
    return df


# Methods for taking OHLC data and creating a list of stocks that fit the predetermined buy parameters, 
# Need multiple methods because of API limit
def makelist1(set):
    x=1 #iterable value to loop through tickers
    for i in set:
        bars = barsets1[(i)]
        db = make_df(bars)
        signal = (db['Trade'])
        var = signal.tail(1)
        bools = var.str.contains('XXXXXXX')
        try:
            if bools[99] == True:
                print(i)
        except KeyError:
            print(f"Incomplete data for {i} KeyError at line 99")
        x+=1

def makelist2(set):
    x=1 #iterable value to loop through tickers
    for i in set:
        bars = barsets2[(i)]
        db = make_df(bars)
        signal = (db['Trade'])
        var = signal.tail(1)
        bools = var.str.contains('XXXXXXX')
        try:
            if bools[99] == True:
                print(i)
        except KeyError:
            print(f"Incomplete data for {i} KeyError at line 99")
        x+=1

def makelist3(set):
    x=1 #iterable value to loop through tickers
    for i in set:
        bars = barsets3[(i)]
        db = make_df(bars)
        signal = (db['Trade'])
        var = signal.tail(1)
        bools = var.str.contains('XXXXXXX')
        try:
            if bools[99] == True:
                print(i)
        except KeyError:
            print(f"Incomplete data for {i} KeyError at line 99")
        x+=1

def makelist4(set):
    x=1 #iterable value to loop through tickers
    for i in set:
        bars = barsets4[(i)]
        db = make_df(bars)
        signal = (db['Trade'])
        var = signal.tail(1)
        bools = var.str.contains('XXXXXXX')
        try:
            if bools[99] == True:
                print(i)
        except KeyError:
            print(f"Incomplete data for {i} KeyError at line 99")
        x+=1

def makelist5(set):
    x=1 #iterable value to loop through tickers
    for i in set:
        bars = barsets5[(i)]
        db = make_df(bars)
        signal = (db['Trade'])
        var = signal.tail(1)
        bools = var.str.contains('XXXXXXX')
        try:
            if bools[99] == True:
                print(i)
        except KeyError:
            print(f"Incomplete data for {i} KeyError at line 99")
        x+=1

def makelist6(set):
    x=1 #iterable value to loop through tickers
    for i in set:
        bars = barsets6[(i)]
        db = make_df(bars)
        signal = (db['Trade'])
        var = signal.tail(1)
        bools = var.str.contains('XXXXXXX')
        try:
            if bools[99] == True:
                print(i)
        except KeyError:
            print(f"Incomplete data for {i} KeyError at line 99")
        x+=1

def makelist7(set):
    x=1 #iterable value to loop through tickers
    for i in set:
        bars = barsets7[(i)]
        db = make_df(bars)
        signal = (db['Trade'])
        var = signal.tail(1)
        bools = var.str.contains('XXXXXXX')
        if bools[99] == True:
            print(i)
        else:
            continue
        x+=1

makelist1(set1)
makelist2(set2)
makelist3(set3)
makelist4(set4)
makelist5(set5)
makelist6(set6)
#makelist7(set7)





# Test code for calling get_ohlc_data and getting 60 day's ohlc data + signals
# stok = barsets6['PYPL']
# AAPL = make_df(stok)
# print(AAPL)


