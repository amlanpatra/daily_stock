import datetime
import internet
import tsend
import time
import indices
import merged
import nifty100_volatility
import candlesticks4


def now():
    now = datetime.datetime.now().hour
    return now


global g
while (datetime.datetime.today().isoweekday() != 6
       or datetime.datetime.today().isoweekday() != 7):
    now = datetime.datetime.now()
    while now.hour >= 9 and (1 if now.hour < 15 else 1 if (now.hour == 15 and now.minute <= 15) else 0):
        g = 0
        min = now.minute
        if (min == 0 or min == 5 or min == 10 or min == 15 or min == 20 or min == 25 or min == 30 or min == 35 or min == 40 or min == 45 or min == 50 or min == 55):
            # TODO: above timeframe is temporary. It's  for 5min chart at ALL times, it must be removed for 15m and 1hr times
            a = candlesticks4.candlesticks(
                indices.nifty50, '5m', quantity=5)
            tsend.min5psend("5min Change : {}".format(
                a.most_change(300, 1500)))
            del a
            print("Sleeping for 1min after 5min data sent")
            time.sleep(60)
        else:
            print("Sleeping for 15secs as minute is : {}".format(
                datetime.datetime.now().minute))
            time.sleep(15)
        now = datetime.datetime.now()

    if datetime.datetime.now().hour < 19:
        print("Sleeping for 16mins")
        time.sleep(1000)

    if datetime.datetime.now().hour >= 19:
        try:
            nifty100_volatility.daily_volatility_pdf_send()
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

        except:
            pass

    break
print("Daily Program Finished\n")
