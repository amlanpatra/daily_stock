import datetime
import internet
import tsend
import time
import daily_change
import indices
import merged
import candlesticks


def now():
    now = datetime.datetime.now().hour
    return now


global g
while (datetime.datetime.today().isoweekday() != 6
       or datetime.datetime.today().isoweekday() != 7):
    now = datetime.datetime.now()

    while now.hour >= 9 and (1 if now.hour < 15 else 1 if (now.hour == 15 and now.minute <= 15) else 0):
        g = 0
        try:
            min = now.minute
            if (min == 0 or min == 5 or min == 10 or min == 15 or min == 20 or min == 25 or min == 30 or min == 35 or min == 40 or min == 45 or min == 50 or min == 55):
                """
                if (min == 5 or min == 10 or min == 20 or min == 25 or min == 35 or min == 40 or min == 50 or min == 55):
                    tsend.psend("5min Sector :  {}".format(
                        daily_change.max_daily_change(indices.nifty_sectors, "5m", add_ns=0)))
                    tsend.psend("5min Nifty50 : {}".format(
                        daily_change.max_daily_change(indices.nifty50, "5m", 10)))
                    tsend.psend("5min Nifty_next50 :{}".format(
                        daily_change.max_daily_change(indices.nifty_next50, "5m", 10)))
                    time.sleep(60)
"""
                if min == 0 or min == 15 or min == 30 or min == 45:
                    tsend.psend("15min nifty_next50 :{}".format(
                        daily_change.max_daily_change(indices.nifty_next50, "15m", 15)))
                    tsend.psend("15min nifty50 :  {}".format(
                        daily_change.max_daily_change(indices.nifty50, "15m", 15)))
                    tsend.send("15 min Sector : {}".format(
                        daily_change.max_daily_change(indices.nifty_sectors, "15m", add_ns=0)))

                    print("Sleeping for 1min as new data sent")
                    if min != 0:
                        time.sleep(60)

                if min == 0 and now.hour > 9:
                    tsend.psend("Hourly nifty_next50 : \n {}".format(
                        daily_change.max_daily_change(indices.nifty_next50, '1h', 15)))
                    tsend.psend("Hourly nifty50 : \n {}".format(
                        daily_change.max_daily_change(indices.nifty50, '1h', 15)))
                    tsend.send("hourly Sectors : {}".format(
                        daily_change.max_daily_change(indices.nifty_sectors, '1h', add_ns=0)))
                    tsend.psend("Doji : {}".format(candlesticks.doji(
                        (indices.nifty50 + indices.nifty_next50), '1h', 20)))
                    print("Sleeping for 1min as Hourly data sent")
                    time.sleep(60)

            else:
                print("Sleeping for 15secs as minute is : {}".format(
                    datetime.datetime.now().minute))
                time.sleep(15)
            now = datetime.datetime.now()
        except:
            if internet.connect():
                tsend.psend("Error occurred in day time script")
            else:
                while (not internet.connect()) and datetime.datetime.now().hour < 15:
                    g += 50
                    time.sleep(g)

    if datetime.datetime.now().hour == 15:
        print("Sleeping for 16mins")
        time.sleep(1000)

    if datetime.datetime.now().hour >= 15:
        try:
            merged.trend("nifty_next50", indices.nifty_next50)
            tsend.psend("Daily nifty_next50 change : \n {}".format(
                daily_change.max_daily_change(indices.nifty_next50)))
            merged.trend("nifty50", indices.nifty50)
            tsend.psend("Daily nifty50 change : \n {}".format(
                daily_change.max_daily_change(indices.nifty50)))
            tsend.psend("Daily most changed sector : \n {}".format(
                daily_change.max_daily_change(indices.nifty_sectors, add_ns=0)))

        except:
            if internet.connect():
                tsend.psend("Error occurred in night time script")
            else:
                while (not internet.connect()) and (
                        datetime.datetime.now().hour >= 15
                        and datetime.datetime.now().hour < 7):
                    g += 50
                    print(
                        "Error occurred in night script and no internet so sleeping for {} secs "
                        .format(str(g)))
                    time.sleep(g)
"""
    while datetime.datetime.now().hour > 15 or datetime.datetime.now().hour < 9:
        if datetime.datetime.now().hour == 8:
            time.sleep(600)
        else:
            # since todays 24 hours + 9 hours of next day
            time_left = 33 - datetime.datetime.now().hour
            print("Sleeping for {} hours ".format(str(time_left - 1)))
            time.sleep((time_left - 1) * 3600)
"""
