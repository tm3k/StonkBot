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



# Method for getting ohlc data for the stock and 30 day period
def get_ohlc_data(stock,day):
    day_open = stock[day].o
    day_high = stock[day].h 
    day_low = stock[day].l 
    day_close = stock[day].c
    candle_time = stock[day].t 

    
    # print(f'Time:  {candle_time}')
    # print(f'Open:  {day_open}')
    # print(f'High:  {day_high}')
    # print(f'Low:   {day_low}')
    # print(f'Close: {day_close}')
    
    add_to_df(day_open, day_high, day_low, day_close,candle_time)


# Method with lists to hold ohlc vals
def add_to_df(day_open,day_high,day_low,day_close,candle_time):
    
    open_vals = []
    high_vals = []
    low_vals = []
    close_vals = []

    open_vals.append(day_open)
    high_vals.append(day_high)
    low_vals.append(day_low)
    close_vals.append(day_close)

    zippedList = list(zip(open_vals, high_vals, low_vals, close_vals))
    df = pd.DataFrame(zippedList, columns = ['open' , 'high', 'low', 'close'])
    df['time'] = candle_time
    
    

    # Magic code to remove hours minutes and seconds from timestamp, formats code for viewing
    df['time'] = pd.to_datetime(df['time'])
    df['time'] = df['time'].dt.date
    pd.set_option('display.width', None)
    pd.set_option('display.max_rows', 30)
    print(df)



# Test code for calling get_ohlc_data and getting the first(of 30) day's ohlc data
aapl_bars=barsets1['AAPL']
get_ohlc_data(aapl_bars,0)
