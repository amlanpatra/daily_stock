import datetime
import merged
import indices
import daily_change
import time
import tsend
import internet

global g
while(datetime.datetime.today().isoweekday() != 6 or datetime.datetime.today().isoweekday() != 7):
    now = datetime.datetime.now()
    while(now.hour >= 9 and now.hour < 15):
        g = 0
        try:
            if (now.minute == 0 or now.minute == 15 or now.minute == 30 or now.minute == 45):
                tsend.psend("nifty50 at {}".format(datetime.datetime.now()))
                daily_change.max_daily_change(indices.nifty50, '15m')
                time.sleep(5)
                tsend.psend("nifty_next50 at {}".format(
                    datetime.datetime.now()))
                daily_change.max_daily_change(indices.nifty_next50, '15m')
                print("Sleeping for 1min as new data sent")
                time.sleep(60)

            else:
                print("Sleeping for 30secs as minute is : {}".format(
                    datetime.datetime.now().minute))
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

    elif(datetime.datetime.now().hour > 15):
        try:
            merged.trend('nifty_next50', indices.nifty_next50)
            daily_change.max_daily_change(indices.nifty_next50)
            merged.trend('nifty50', indices.nifty50)
            daily_change.max_daily_change(indices.nifty50)
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
