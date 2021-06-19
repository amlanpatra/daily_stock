import pandas as pd
import yfinance as yf
import datetime
import tsend
import daily_vol
import subprocess

now = datetime.datetime.now()
today = datetime.date.today().strftime("%d_%m ")

indices = ['ACC','ADANIENT','ADANIPORTS','ADANIPOWER','AMARAJABAT','AMBUJACEM','APOLLOHOSP','APOLLOTYRE','ASHOKLEY','ASIANPAINT','AUROPHARMA','AXISBANK','BAJAJ-AUTO','BAJAJFINSV','BAJFINANCE','BALKRISIND','BANKBARODA','BATAINDIA','BEL','BERGEPAINT','BHARATFORG','BHARTIARTL','BHEL','BIOCON','BOSCHLTD','BPCL','BRITANNIA','CADILAHC','CANBK','CASTROLIND','CENTURYTEX','CESC','CHOLAFIN','CIPLA','COALINDIA','COLPAL','CONCOR','CUMMINSIND','DABUR','DISHTV','DIVISLAB','DLF','DRREDDY','EICHERMOT','EQUITAS','ESCORTS','EXIDEIND','FEDERALBNK','GAIL','GLENMARK','GMRINFRA','GODREJCP','GRASIM','HAVELLS','HCLTECH','HDFC','HDFCBANK','HEROMOTOCO','HINDALCO','HINDPETRO','HINDUNILVR','IBULHSGFIN','ICICIBANK','ICICIPRULI','IDEA','IDFCFIRSTB','IGL','INDIGO','INDUSINDBK','INFRATEL','INFY','IOC','ITC','JINDALSTEL','JSWSTEEL','JUBLFOOD','JUSTDIAL','KOTAKBANK','L&TFH','LICHSGFIN','LT','LUPIN','M&M','M&MFIN','MANAPPURAM','MARICO','MARUTI','MCDOWELL-N','MFSL','MGL','MINDTREE','MOTHERSUMI','MRF','MUTHOOTFIN','NATIONALUM','NBCC','NCC','NESTLEIND','NMDC','NTPC','OIL','ONGC','PAGEIND','PEL','PETRONET','PFC','PIDILITIND','PNB','POWERGRID','PVR','RAMCOCEM','RBLBANK','RECLTD','RELIANCE','SAIL','SBIN','SBILIFE','SHREECEM','SIEMENS','SRF','SRTRANSFIN','SUNPHARMA','SUNTV','TATACHEM','TATAMOTORS','TATAMTRDVR','TATAPOWER','TATASTEEL','TCS','TECHM','TITAN','TORNTPHARM','TORNTPOWER','TVSMOTOR','UBL','UJJIVAN','ULTRACEMCO','UPL','VEDL','VOLTAS','WIPRO','YESBANK','ZEEL']
# NIITTECH is removed, because of IndexError: single positional indexer is out-of-bounds

for sending_dots in range(10):
    tsend.send(".")

tsend.send("Downward Trend")

for sending_dots in range(2):
    tsend.send(".")
















######################################### PART 1 ::   DAY3_TREND.PY  (FETCHING DATA OF ALL THE STOCKS IN F&O)############################################
per = '4d'
ultimate_3nd = []
ultimate_2nd = []
ultimate_1d  = []
final_volume = []
print(now.time())

for x in indices:
    b = x+'.NS'
    print(b)
    data = yf.download(tickers=b, period=per,interval='1d')
    df = pd.DataFrame(data)
    #print(df)
    day1 = round(df.iloc[0]['Close'], 2)
    day2 = round(df.iloc[1]['Close'], 2)
    day3 = round(df.iloc[2]['Close'], 2)
    day4 = round(df.iloc[3]['Close'], 2)
    change3 = round((day4 - day3), 2)
    change2 = round((day3 - day2), 2)
    change1 = round((day2 - day1), 2)

    if ((change3 < 0) and ((day4 >100) and (day4 < 1000))):
        final_volume.append(b)
        ultimate_1d.append(x)
        if (change2 < 0):
            ultimate_2nd.append(x)
            if (change1 < 0):
                #tsend.send(x + '                              1d : '+str(change3)+'         2nd : '+ str(change2)+'                    3rd : '+str(change1)+'                          Current Price : '+str(round(df.iloc[3]['Close'], 2)))
                ultimate_3nd.append(x)
for i in ultimate_2nd:
    ultimate_1d.remove(i)
for i in ultimate_3nd:
    ultimate_2nd.remove(i)
print("\n\n\nPrevious 3day downtrend stocks : ",ultimate_3nd)
print("Only 2day downtrend stocks but not 3days: ",ultimate_2nd)
print("Only 1day downtrend : ",ultimate_1d)
print(df)




######################################## PART 2 :: DAILY_TREND.PY   (SAVING FILES IN STOCK ANAYSIS FOLDER)#########################################
full_fo = indices
only_1d = ultimate_1d
only_2d = ultimate_2nd
only_3d = ultimate_3nd
date = today
daily_vol.get_file()
daily_vol.fo(only_3d,(date)+ str(3))
daily_vol.fo(only_2d,(date)+ str(2))
daily_vol.fo(only_1d,(date)+ str(1))
daily_vol.fo(full_fo,(date)+ 'all ')

#### sending the main files  and removing them from directory #########
day3_stk = str((date)+ str(3)+'d F&O.csv')
day2_stk = str((date)+ str(2)+'d F&O.csv')
day1_stk = str((date)+ str(1)+'d F&O.csv')
all_d_stk = str(str(date)+'all '+'d F&O.csv')
main_stk = "Main.csv"

## sending ##
tsend.file_send(day3_stk)
tsend.file_send(day2_stk)
tsend.file_send(day1_stk)
tsend.file_send(all_d_stk)
tsend.file_send(main_stk)

## removing from current directory ##
subprocess.call(("rm "+"Main.csv"),shell=True)
subprocess.call(("rm "+'"{}"'.format(day3_stk)),shell=True)
subprocess.call(("rm "+'"{}"'.format(day2_stk)),shell=True)
subprocess.call(("rm "+'"{}"'.format(day1_stk)),shell=True)
subprocess.call(("rm "+ '"{}"'.format(all_d_stk)),shell=True)




########################### PART 3 :: MULTIPLE_DAY_TREND.PY   (SENDING MESSAGES OF MAX UPTREND DAYS ~LIMIT 10) ####################################
indicesx = ["ok",ultimate_1d,ultimate_2nd,ultimate_3nd]
final_index = indicesx[0]
for f in range(1,4):
    num = f
    text = str(num) + "day trend stocks ::                    Current Date : " + str(now)
    days = 10
    per = str(days)+'d'
    #if ((now.hour>8) and (now.hour < 18)):   #    per = '11d'
    tsend.send(text)
    final_index = indicesx[f]
    for x in final_index:
        b = x+'.NS'
        print(b)
        data = yf.download(tickers=b, period=per,interval='1d')
        df = pd.DataFrame(data)
        tele_send = x+' ::     '
        count = 0
        up_limit = days-1
        diff = -1
        while (diff < 0):
            day_up = round(df.iloc[up_limit]['Close'], 2)
            day_down = round(df.iloc[up_limit-1]['Close'], 2)
            diff = round((day_up - day_down),2)
            count += 1
            up_limit-=1
            tele_send = tele_send + str(count) + 'd : ' + str(diff) + '       '
            #print("Telesend : "+tele_send)
            #print("count : "+str(count)) #print(df)
            #print("Diff : "+str(diff))
        tele_send = tele_send + '       Current Price : '+str(round(df.iloc[9]['Close'], 2))
        tsend.send(str(tele_send))
print(df,"\n")







############# PART 4 : SENDING MESSAGE ACCORDING TO VOLUME SORTED ################################

datax = yf.download(final_volume, period = "1d",interval = "1d",group_by="ticker")
dfxr = pd.DataFrame(datax)

bx = ["Open","High","Low","Adj Close","Close"]
final = []
temp = [[0,0]]
for ixr in final_volume:
    final.append([ixr,dfxr.iloc[0][(ixr,"Volume")]])
    for xvz in bx:
        dfxr = dfxr.drop(columns = [(ixr,xvz)])


def sortSecond(val): 
    return val[1]

final.sort(key=sortSecond,reverse=True) 

tsend.send(".")
tsend.send(".")
tsend.send(".")
tsend.send("Stocks send according to Volume : ")
tsend.send(".")

for sorted_value in final:
	tsend.send(str(sorted_value))







#tsend.send(str(final))
print("\n\n\n",dfxr)




























