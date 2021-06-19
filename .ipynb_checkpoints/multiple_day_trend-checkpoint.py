import pandas as pd
import yfinance as yf
import datetime
import tsend
now = datetime.datetime.now()

indicesx = ['AMBUJACEM', 'CADILAHC', 'CASTROLIND', 'CENTURYTEX', 'COALINDIA', 'CONCOR', 'DLF', 'HAVELLS', 'HINDALCO', 'HINDPETRO', 'ICICIBANK', 'JINDALSTEL', 'LT', 'MANAPPURAM', 'MARICO', 'MCDOWELL-N', 'SBILIFE', 'SRTRANSFIN', 'TATACHEM', 'UBL', 'VEDL', 'VOLTAS', 'WIPRO']

num = 1
































text = str(num) + "day trend stocks ::                    Current Date : " + str(now)
days = 10
per = str(days)+'d'
#if ((now.hour>8) and (now.hour < 18)):
#    per = '11d'
tsend.send(text)
for x in indicesx:
    b = x+'.NS'
    print(b)
    data = yf.download(tickers=b, period=per,interval='1d')
    df = pd.DataFrame(data)
    tele_send = x+' ::     '
    count = 0
    up_limit = days-1
    diff = 1
    while (diff > 0):
        day_up = round(df.iloc[up_limit]['Close'], 2)
        day_down = round(df.iloc[up_limit-1]['Close'], 2)
        diff = round((day_up - day_down),2)
        count += 1
        up_limit-=1
        tele_send = tele_send + str(count) + 'd : ' + str(diff) + '       '
        #print(tele_send)
        #print(count)
        #print(df)
    tele_send = tele_send + '       Current Price : '+str(round(df.iloc[9]['Close'], 2))
    tsend.send(str(tele_send))
print(df)