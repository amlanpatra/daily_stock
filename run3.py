
import datetime
import internet
import tsend
import time
import daily_change
import indices
import merged

def now():
    now = datetime.datetime.now().hour
    return now

global g
while(datetime.datetime.today().isoweekday() != 6 or datetime.datetime.today().isoweekday() != 7):
    now = datetime.datetime.now()
    while(now.hour >= 9 and now.hour < 15):
        g = 0
        try:
            min = now.minute
            if (min == 1 or min == 6 or min == 11 or min == 16 or min == 21 or min == 26 or min == 31 or min == 36 or min == 41 or min == 46 or min == 51 or min == 56):
                tsend.psend("5 min Sector : {}".format(daily_change.max_daily_change(indices.nifty_sectors,'5m',add_ns=0)))
                tsend.psend("Nifty50 : {}".format(daily_change.max_daily_change(indices.nifty50, '5m', 10)))
                tsend.psend("Nifty_next50 : {}".format(daily_change.max_daily_change(indices.nifty_next50, '5m', 10)))
                
                if (min == 1 or min == 16 or min == 31 or min == 46):
                    tsend.psend("15 min Sector : {}".format(
                       daily_change.max_daily_change(indices.nifty_sectors, '15m', add_ns=0)))
                    tsend.psend("15min nifty50 : \n {}".format(daily_change.max_daily_change(indices.nifty50, '15m',15)))
                    tsend.psend("15min nifty_next50 : \n {}".format(daily_change.max_daily_change(indices.nifty_next50, '15m',15)))
                    print("Sleeping for 1min as new data sent")

            else:
                print("Sleeping for 30secs as minute is : {}".format(datetime.datetime.now().minute))
                time.sleep(30)
            now = datetime.datetime.now()
        except:
            if (internet.connect()):
                tsend.psend("Error occurred in day time script")
            else:
                while((not internet.connect()) and datetime.datetime.now().hour < 15):
                    g += 50
                    time.sleep(g)



    if(datetime.datetime.now().hour == 15):
        print("Sleeping for 3900 secs")
        time.sleep(3900)

    if(datetime.datetime.now().hour > 15):
        try:
            merged.trend('nifty_next50', indices.nifty_next50)
            tsend.psend("Daily nifty_next50 change : \n {}".format(daily_change.max_daily_change(indices.nifty_next50)))
            merged.trend('nifty50', indices.nifty50)
            tsend.psend("Daily nifty50 change : \n {}".format(daily_change.max_daily_change(indices.nifty50)))
            tsend.psend("Daily most changed sector : {}".format(daily_change.max_daily_change(indices.nifty_sectors,add_ns=0)))
        except:
            if (internet.connect()):
                tsend.psend("Error occurred in night time script")
            else:
                while((not internet.connect()) and (datetime.datetime.now().hour >= 15 and datetime.datetime.now().hour < 7)):
                    g += 50
                    print(
                        "Error occurred in night script and no internet so sleeping for {} secs ".format(str(g)))
                    time.sleep(g)

    while(datetime.datetime.now().hour > 15 or datetime.datetime.now().hour < 9):
        if (datetime.datetime.now().hour == 8):
            time.sleep(600)
        else:
            # since todays 24 hours + 9 hours of next day
            time_left = 33 - datetime.datetime.now().hour
            print("Sleeping for {} hours ".format(str(time_left - 1)))
            time.sleep((time_left-1)*3600)
