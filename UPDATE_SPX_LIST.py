import yfinance as yf
import pandas as pd

# Download the S&P 500 table from Wikipedia
url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
table = pd.read_html(url)
sp500_table = table[0]

# Extract the ticker symbols
sp500_tickers = sp500_table['Symbol'].tolist()

# Remove any tickers with problematic characters (if needed)
sp500_tickers = [ticker.replace('.', '-') for ticker in sp500_tickers]

print(sp500_tickers)
