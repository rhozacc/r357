import matplotlib.pyplot as plt
from functools import reduce
import pandas as pd
import yfinance as yf
import os

# indices = ["^GSPC", "^HSI", "^FTSE", "^SSEC", "^N225", "^GDAXI"]
indices = ["^VIX", "^TNX", "^IRX", "^FVX", "LQD"]
data = [pd.DataFrame(yf.Ticker(i).history(start="2008-9-15", end="2008-12-12")) for i in indices]

rets, closes = pd.DataFrame(), pd.DataFrame()

for i, df in enumerate(data):
    rets[i] = df["Close"].pct_change()
    closes[i] = df["Close"]/df["Close"][0]
    df.to_excel(os.getcwd()+"/Downloaded/"+indices[i].replace("^","")+".xls")
	    
rets.columns, closes.columns = indices, indices
rets.plot()
closes.plot()