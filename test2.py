import pandas as pd
import indices
import candlesticks3
import tsend

a = candlesticks3.candlesticks(indices.nifty100, intrvl='1d', quantity=5)
print(a.hammer())
print(a.doji())
print(a.most_change())
