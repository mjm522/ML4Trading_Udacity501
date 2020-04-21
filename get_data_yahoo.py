import pandas as pd
from datetime import date
from pandas_datareader import data as pdr

# Tickers list
# ticker_list=['AAPL', 'SPY', 'GLD', 'XOM', 'IBM'] 
ticker_list=['GOOG'] 

today = date.today()

start_date="20000101"
end_date="20200131"

def getData(ticker):
    print(ticker)
    data = pdr.get_data_yahoo(ticker, start=start_date, end=today)
    dataname= ticker
    SaveData(data, ticker)

def SaveData(df, filename):
    df.to_csv('./data/'+filename+'.csv')

for tik in ticker_list:
    getData(tik)
