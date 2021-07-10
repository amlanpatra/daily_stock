import datetime
import internet
import tsend
import time
import indices
import merged
import candlesticks3
import nifty100_volatility


def now():
    now = datetime.datetime.now().hour
    return now


global g
while (datetime.datetime.today().isoweekday() != 6
       or datetime.datetime.today().isoweekday() != 7):
    now = datetime.datetime.now()
# FIXME: now.hour >=9 msut be done; changed for specific reason
    while now.hour >= 8 and (1 if now.hour < 15 else 1 if (now.hour == 15 and now.minute <= 15) else 0):
        g = 0
        try:
            min = now.minute
            if (min == 0 or min == 5 or min == 10 or min == 15 or min == 20 or min == 25 or min == 30 or min == 35 or min == 40 or min == 45 or min == 50 or min == 55):
                if (min == 5 or min == 10 or min == 20 or min == 25 or min == 35 or min == 40 or min == 50 or min == 55):
                    a = candlesticks3.candlesticks(
                        indices.nifty100, '5m', quantity=5)
                    tsend.min5psend("5min Doji : {}".format(a.doji()))
                    tsend.min5psend("5min Hammer : {}".format(a.hammer()))
                    tsend.min5psend("5min Change : {}".format(a.most_change()))
                    del a
                    print("Sleeping for 1min after 5min data sent")
                    time.sleep(60)

                if min == 0 or min == 15 or min == 30 or min == 45:
                    a = candlesticks3.candlesticks(
                        indices.nifty_sectors, intrvl='15m', add_ns=0)
                    tsend.pkpsend("15min Sectors : {}".format(a.most_change()))
                    del a
                    b = candlesticks3.candlesticks(
                        indices.nifty100, '15m', quantity=5)
                    tsend.pkpsend("15min Doji : {}".format(b.doji()))
                    tsend.pkpsend("15min Hammer : {}".format(b.hammer()))
                    tsend.pkpsend("15min Change :  {}".format(b.most_change()))
                    del b
                    print("Sleeping for 1min as new data sent")
                    if (min != 0):
                        time.sleep(60)

                if min == 0 and now.hour > 9:
                    a = candlesticks3.candlesticks(
                        indices.nifty_sectors, intrvl='1h', add_ns=0)
                    tsend.psend(
                        "1h Sectors : {}".format(a.most_change()))
                    del a
                    b = candlesticks3.candlesticks(
                        indices.nifty100, '1h', quantity=5)
                    tsend.psend("1h Doji : {}".format(b.doji()))
                    tsend.psend("1h Hammer : {}".format(b.hammer()))
                    tsend.psend("1h Change :  {}".format(b.most_change()))
                    del b

                    print("Sleeping for 1min as Hourly data sent")
                    time.sleep(60)

            else:
                print("Sleeping for 15secs as minute is : {}".format(
                    datetime.datetime.now().minute))
                time.sleep(15)
            now = datetime.datetime.now()
        except Exception as e:
            if internet.connect():
                tsend.psend(
                    "Error occurred in day time script with exception : {}".format(e.message))
            else:
                while (not internet.connect()) and datetime.datetime.now().hour < 15:
                    g += 50
                    time.sleep(g)

    if datetime.datetime.now().hour < 19:
        # if datetime.datetime.now().hour == 15:
        print("Sleeping for 16mins")
        time.sleep(1000)

    # if datetime.datetime.now().hour >= 15:
    if datetime.datetime.now().hour >= 19:
        try:
            nifty100_volatility.daily_volatility_pdf_send()
            merged.trend("UP/DOWN change : ",
                         (indices.nifty_next50 + indices.nifty50), lmt=10)

            a = candlesticks3.candlesticks(indices.nifty_sectors, add_ns=0)
            tsend.psend(
                "Daily most changed sector : {}".format(a.most_change()))
            del a

            b = candlesticks3.candlesticks(indices.nifty100, quantity=10)

            tsend.psend(
                "Daily nifty100 top 10 Change : \n {}".format(b.most_change()))
            tsend.psend("Daily nifty100 10 Doji: {}".format(b.doji()))
            # tsend.psend("Daily nifty100 Hammer : {}".format(b.hammer()))

        except Exception as e:
            if internet.connect():
                tsend.psend(
                    "Error occurred in night time script with error : {}".format(e.message))
            else:
                while (not internet.connect()) and (
                        datetime.datetime.now().hour >= 15
                        and datetime.datetime.now().hour < 7):
                    g += 50
                    print(
                        "Error occurred in night script and no internet so sleeping for {} secs "
                        .format(str(g)))
                    time.sleep(g)

    break
print("Daily Program Finished\n")
