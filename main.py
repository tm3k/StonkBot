import creds
from finta import TA
import yfinance as yf
import spx500
import pandas as pd
import numpy as np
from datetime import datetime
import time as t

def make_df(stock):
    data = stock[['Open', 'High', 'Low', 'Close']].copy()
    data.columns = ['open', 'high', 'low', 'close']
    data['%BB'] = np.nan_to_num(TA.PERCENT_B(data))
    data['Trade'] = data['%BB'].apply(lambda x: 'Oversold' if x < -0.05 else '')
    return data


def makelist(stock_set):
    for symbol in stock_set:
        try:
            stock_data = yf.download(symbol, start='2021-01-01', end='2023-03-18', progress=False)
            df = make_df(stock_data)
            signal = df['Trade'].tail(1)
            if signal.iloc[-1] == 'Oversold':
                print(f"${symbol} - ${df['close'].iloc[-1].round(2)} Oversold")
        except KeyError:
            print(f"Incomplete data for {symbol} KeyError at line 99")

while True:
    print(datetime.now().strftime("\n%Y-%m-%d %H:%M PST"))
    print('Volatility Watchlist:\n')
    for i in range(0, 1100, 100):
        stock_set = spx500.stocklist[i:i+100]
        makelist(stock_set)

    print("\nScanning again in 10 minutes.\nWaiting...")
    t.sleep(600)
