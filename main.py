import creds
from finta import TA
import alpaca_trade_api as tradeapi
import spx500
import pandas as pd
import numpy as np
from datetime import date, time, datetime
import time as t


while True:
    # Creates API object for OHLC
    api = tradeapi.REST(creds.api_key, creds.api_secret, api_version='v1') 

    # Can only call 100 stocks at a time thru the api so had to split it up
    set1 = spx500.stocklist[:100]
    set2 = spx500.stocklist[100:200]
    set3 = spx500.stocklist[200:300]
    set4 = spx500.stocklist[300:400]
    set5 = spx500.stocklist[400:500]
    set6 = spx500.stocklist[500:600]
    set7 = spx500.stocklist[600:700]
    set8 = spx500.stocklist[700:800]
    set8 = spx500.stocklist[800:900]
    #set9 = spx500.stocklist[900:1000]
    #set10 = spx500.stocklist[1000:1100]


    #ohlc data for each set of stocks
    barsets1 = api.get_barset(set1, timeframe = '1D', limit = 100)
    barsets2 = api.get_barset(set2, timeframe = '1D', limit = 100)
    barsets3 = api.get_barset(set3, timeframe = '1D', limit = 100)
    barsets4 = api.get_barset(set4, timeframe = '1D', limit = 100)
    barsets5 = api.get_barset(set5, timeframe = '1D', limit = 100)
    barsets6 = api.get_barset(set6, timeframe = '1D', limit = 100)
    barsets7 = api.get_barset(set7, timeframe = '1D', limit = 100)
    barsets8 = api.get_barset(set8, timeframe = '1D', limit = 100)
    #barsets9 = api.get_barset(set9, timeframe = '1D', limit = 100)
    #barsets10 = api.get_barset(set10, timeframe = '1D', limit = 100)


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
    
    def makelist(set, barset):
        x=1 #iterable value to loop through tickers
        for i in set:
            bars = barset[(i)]
            db = make_df(bars)
            signal = (db['Trade'])
            price = db['close']
            var = signal.tail(1)
            bools = var.str.contains('XXXXXXX')
            today = date.today()  # Code for writing to file with date and time.
            now = datetime.now()
            time = now.strftime(" H%H M%M")
            writer = open(f"{today} {time}.txt", 'a') #cant write : to a filename    
            try:
                if bools[99] == True:
                    print(f"${i} - ${price[99].round(2)}") #prints stock ticker to console
                    writer.write(f"{i}\n") #writes stock ticker to file
                    
            except KeyError:
                print(f"Incomplete data for {i} KeyError at line 99")
            x+=1

    today = datetime.now()
    today = today.strftime("\n%Y-%m-%d %H:%M PST")    
    print(today)
    print('Volatility Watchlist:\n')
    makelist(set1, barsets1)
    makelist(set2, barsets2)
    makelist(set3, barsets3)
    makelist(set4, barsets4)
    makelist(set5, barsets5)
    makelist(set6, barsets6)
    makelist(set7, barsets7)
    makelist(set8, barsets8)
    #makelist(set9, barsets9)
    #makelist(set10, barsets10)

    # waits 300 seconds aka 5 minutes after finish writing completed_list ^^ 
    # runs program again and checks for differences in the 2 lists
    # 5 min = 300
    # 10 min = 600
    # 15 min = 900
    # 30 min = 1800
    print("\nScanning again in 10 minutes.\nWaiting...")
    t.sleep(600)
    
