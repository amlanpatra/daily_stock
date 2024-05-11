import candlesticks4
import indices
import merged
import tsend
merged.trend("UP/DOWN change : ",
             (indices.nifty50), lmt=10)

a = candlesticks4.candlesticks(indices.nifty_sectors, add_ns=0)
tsend.psend(
    "Daily most changed sector : {}".format(a.most_change()))
del a

b = candlesticks4.candlesticks(indices.nifty50, quantity=10)
tsend.send(
    "Top change : \n {}".format(b.most_change(300, 1500)))
del b
