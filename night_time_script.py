import datetime
import candlesticks4
import merged
import indices
import nifty100_volatility
import tsend

index = indices.nifty50
qty = 10
# choices : 1) nifty50, nifty100 2) lmt = 10


def run(index, qty):
    if datetime.datetime.now().hour >= 19:
        try:
            nifty100_volatility.daily_volatility_pdf_send()
            merged.trend("UP/DOWN change : ",
                         (index), lmt=10)
            a = candlesticks4.candlesticks(index, add_ns=0)
            tsend.psend(
                "Daily most changed sector : {}".format(a.most_change()))
            del a
            b = candlesticks4.candlesticks(index, quantity=qty)
            tsend.send(
                "Top change : \n {}".format(b.most_change(300, 1500)))
            del b
        except:
            pass
    """
    nifty50 / nifty100
    limit
    """
