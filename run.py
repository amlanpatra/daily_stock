import datetime
import merged
import indices
import daily_change
import time
import tsend

now = datetime.datetime.now()
while(now.hour >= 9 and now.hour < 15):
    try:
        if (now.minute == 0) or (now.minute == 15):
            tsend.psend("nifty50 at {}".format(datetime.datetime.now()))
            daily_change.max_daily_change(indices.nifty50, '15m')
            time.sleep(5)
            tsend.psend("nifty_next50 at {}".format(datetime.datetime.now()))
            daily_change.max_daily_change(indices.nifty_next50, '15m')
            print("Sleeping for 1min as new data sent")
            time.sleep(60)
        elif (now.minute == 30) or (now.minute == 45):
            tsend.psend("nifty50 at {}".format(datetime.datetime.now()))
            daily_change.max_daily_change(indices.nifty50, '15m')
            time.sleep(5)
            tsend.psend("nifty_next50 at {}".format(datetime.datetime.now()))
            daily_change.max_daily_change(indices.nifty_next50, '15m')
            print("Sleeping for 1min as new data sent")
            time.sleep(60)
        else:
            print("Sleeping for 30secs as minute is : {}".format(
                datetime.datetime.now().minute))
            time.sleep(30)
        now = datetime.datetime.now()
    except:
        tsend.psend("Error occurred in day time script")

if(datetime.datetime.now().hour == 15):
    print("Sleeping for 3900 secs")
    time.sleep(3900)
try:
    merged.trend('nifty_next50', indices.nifty_next50)
    daily_change.max_daily_change(indices.nifty_next50)
    merged.trend('nifty50', indices.nifty50)
    daily_change.max_daily_change(indices.nifty50)
except:
    tsend.psend("Error occurred in evening script")
