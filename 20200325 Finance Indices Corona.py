import matplotlib.pyplot as plt
from functools import reduce
import pandas as pd
import yfinance as yf

indices = ["^GSPC", "^HSI", "^FTSE", "^SSEC", "^N225", "^GDAXI"]
data = [pd.DataFrame(yf.Ticker(i).history(start="2020-2-21")) for i in indices]

rets, closes = pd.DataFrame(), pd.DataFrame()

for i, df in enumerate(data):
    rets[i] = df["Close"].pct_change()
    closes[i] = df["Close"]/df["Close"][0]
    
rets.columns, closes.columns = indices, indices
rets.plot()
closes.plot()