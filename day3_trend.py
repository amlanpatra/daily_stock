import pandas as pd
import yfinance as yf
import datetime
import tsend
now = datetime.datetime.now()

indices = ['ACC','ADANIENT','ADANIPORTS','ADANIPOWER','AMARAJABAT','AMBUJACEM','APOLLOHOSP','APOLLOTYRE','ASHOKLEY','ASIANPAINT','AUROPHARMA','AXISBANK','BAJAJ-AUTO','BAJAJFINSV','BAJFINANCE','BALKRISIND','BANKBARODA','BATAINDIA','BEL','BERGEPAINT','BHARATFORG','BHARTIARTL','BHEL','BIOCON','BOSCHLTD','BPCL','BRITANNIA','CADILAHC','CANBK','CASTROLIND','CENTURYTEX','CESC','CHOLAFIN','CIPLA','COALINDIA','COLPAL','CONCOR','CUMMINSIND','DABUR','DISHTV','DIVISLAB','DLF','DRREDDY','EICHERMOT','EQUITAS','ESCORTS','EXIDEIND','FEDERALBNK','GAIL','GLENMARK','GMRINFRA','GODREJCP','GRASIM','HAVELLS','HCLTECH','HDFC','HDFCBANK','HEROMOTOCO','HINDALCO','HINDPETRO','HINDUNILVR','IBULHSGFIN','ICICIBANK','ICICIPRULI','IDEA','IDFCFIRSTB','IGL','INDIGO','INDUSINDBK','INFRATEL','INFY','IOC','ITC','JINDALSTEL','JSWSTEEL','JUBLFOOD','JUSTDIAL','KOTAKBANK','L&TFH','LICHSGFIN','LT','LUPIN','M&M','M&MFIN','MANAPPURAM','MARICO','MARUTI','MCDOWELL-N','MFSL','MGL','MINDTREE','MOTHERSUMI','MRF','MUTHOOTFIN','NATIONALUM','NBCC','NCC','NESTLEIND','NIITTECH','NMDC','NTPC','OIL','ONGC','PAGEIND','PEL','PETRONET','PFC','PIDILITIND','PNB','POWERGRID','PVR','RAMCOCEM','RBLBANK','RECLTD','RELIANCE','SAIL','SBILIFE','SBIN','SHREECEM','SIEMENS','SRF','SRTRANSFIN','SUNPHARMA','SUNTV','TATACHEM','TATAMOTORS','TATAMTRDVR','TATAPOWER','TATASTEEL','TCS','TECHM','TITAN','TORNTPHARM','TORNTPOWER','TVSMOTOR','UBL','UJJIVAN','ULTRACEMCO','UPL','VEDL','VOLTAS','WIPRO','YESBANK','ZEEL']
indices = ['NIITTECH']
indices = ['HCLTECH']

#def trend(period,stock):

per = '4d'
#if ((now.hour>9) and (now.hour < 18)):
#    per = '5d'
ultimate_3nd = []
ultimate_2nd = []
ultimate_1d = []
print(now.time())

#tsend.send("3days Uptrend stocks ::")
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

    if ((change3 > 0) and ((day4 >100) and (day4 < 1000))):
        ultimate_1d.append(x)
        if (change2 > 0):
            ultimate_2nd.append(x)
            if (change1 > 0):
                #tsend.send(x + '                              1d : '+str(change3)+'         2nd : '+ str(change2)+'                    3rd : '+str(change1)+'                          Current Price : '+str(round(df.iloc[3]['Close'], 2)))
                ultimate_3nd.append(x)

for i in ultimate_2nd:
    ultimate_1d.remove(i)
for i in ultimate_3nd:
    ultimate_2nd.remove(i)




print("\n\n\nPrevious 3day uptrend stocks : ",ultimate_3nd)
print("Only 2day uptrend stocks but not 3days: ",ultimate_2nd)
print("Only 1day uptrend : ",ultimate_1d)
print(df)



