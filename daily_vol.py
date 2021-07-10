import pandas as pd
import os
import datetime
import wget

#print('The current directory is :', os.getcwd())


# First take current date in format '1712020'. Second find the day, ie. Friday, Saturday or Sunday. Third if Friday, modify : 17012020
# If Saturday(ie.index 5) change date to 1612020. Then change to 16012020.
# If Sunday(ie.index 6) change date to 1512020. Then change to 15012020.
# Get the file downloaded as : 'DV 17.01 main.csv'
# 'dv'+

def get_file(changing_name='Main.csv'):
    now = datetime.datetime.now()
    d = str(now.day)
    m = now.month
    m1 = str(m)
    y = str(now.year)

    #   Initial date ie. '1712020'
    date = (d + m1 + y)

    # New date of finding day, ie. '17 1 2020'
    new_date = (d + ' ' + m1 + ' ' + y)
    gamma = datetime.datetime.strptime(new_date, '%d %m %Y').weekday()

    if gamma == 5:
        d = int(float(d)) - 1
        d = str(d)
    elif gamma == 6:
        d = int(float(d)) - 2
        d = str(d)
    elif gamma == 0 and (now.hour) < 16:
        d = int(float(d)) - 3
        d = str(d)

    elif gamma in [1, 2, 3, 4] and (now.hour) < 16:
        d = int(float(d)) - 1
        d = str(d)

    if m < 10:
        m = '0' + str(m)
        m = str(m)
    if int(float(d)) < 10:
        d = '0' + d

    date = (d + m + y)
    datex = str(date)
    # print(date)

    # Getting the file
    global final_url
    final_url = str(
        'https://www1.nseindia.com/archives/nsccl/volt/CMVOLT_') + datex + ('.CSV')
    global changing_date
    # global changing_name
    #changing_date = ("dv " + d + '.' + m)
    #changing_name = (changing_date + ' Main.csv')
    # changing_name = ('Main.csv')
    print(final_url)
    get_file = wget.download(final_url, changing_name)


# get_file()

# Main Algorithm
#a = pd.read_csv(changing_name, header=0, index_col=1)
okokok = ['ACC', 'ADANIENT', 'ADANIPORTS', 'ADANIPOWER', 'AMARAJABAT', 'AMBUJACEM', 'APOLLOHOSP', 'APOLLOTYRE', 'ASHOKLEY',
          'ASIANPAINT', 'AUROPHARMA', 'AXISBANK', 'BAJAJ-AUTO', 'BAJAJFINSV', 'BAJFINANCE', 'BALKRISIND', 'BANKBARODA',
          'BATAINDIA', 'BEL', 'BERGEPAINT', 'BHARATFORG', 'BHARTIARTL', 'BHEL', 'BIOCON', 'BOSCHLTD', 'BPCL', 'BRITANNIA',
          'CADILAHC', 'CANBK', 'CASTROLIND', 'CENTURYTEX', 'CESC', 'CHOLAFIN', 'CIPLA', 'COALINDIA', 'COLPAL', 'CONCOR',
          'CUMMINSIND', 'DABUR', 'DISHTV', 'DIVISLAB', 'DLF', 'DRREDDY', 'EICHERMOT', 'EQUITAS', 'ESCORTS', 'EXIDEIND',
          'FEDERALBNK', 'GAIL', 'GLENMARK', 'GMRINFRA', 'GODREJCP', 'GRASIM', 'HAVELLS', 'HCLTECH', 'HDFC', 'HDFCBANK',
          'HEROMOTOCO', 'HINDALCO', 'HINDPETRO', 'HINDUNILVR', 'IBULHSGFIN', 'ICICIBANK', 'ICICIPRULI', 'IDEA', 'IDFCFIRSTB',
          'IGL', 'INDIGO', 'INDUSINDBK', 'INFRATEL', 'INFY', 'IOC', 'ITC', 'JINDALSTEL', 'JSWSTEEL', 'JUBLFOOD', 'JUSTDIAL',
          'KOTAKBANK', 'L&TFH', 'LICHSGFIN', 'LT', 'LUPIN', 'M&M', 'M&MFIN', 'MANAPPURAM', 'MARICO', 'MARUTI', 'MCDOWELL-N',
          'MFSL', 'MGL', 'MINDTREE', 'MOTHERSUMI', 'MRF', 'MUTHOOTFIN', 'NATIONALUM', 'NBCC', 'NCC', 'NESTLEIND', 'NIITTECH',
          'NMDC', 'NTPC', 'OIL', 'ONGC', 'PAGEIND', 'PEL', 'PETRONET', 'PFC', 'PIDILITIND', 'PNB', 'POWERGRID', 'PVR',
          'RAMCOCEM', 'RBLBANK', 'RECLTD', 'RELIANCE', 'SAIL', 'SBIN', 'SHREECEM', 'SIEMENS', 'SRF', 'SRTRANSFIN',
          'SUNPHARMA', 'SUNTV', 'TATACHEM', 'TATAMOTORS', 'TATAMTRDVR', 'TATAPOWER', 'TATASTEEL', 'TCS', 'TECHM', 'TITAN',
          'TORNTPHARM', 'TORNTPOWER', 'TVSMOTOR', 'UBL', 'UJJIVAN', 'ULTRACEMCO', 'UPL', 'VEDL', 'VOLTAS', 'WIPRO',
          'YESBANK', 'ZEEL']
# 'TATAGLOBAL', was above in the list


def fo(c, x):
    import os
    a = pd.read_csv('Main.csv', header=0, index_col=1)
    # this is changing into the desired directory and so not compulsory
    # os.chdir("/Users/amlanpatra/Desktop/test")
    list_of_tables = []
    for i in c:
        try:
            b = a.loc[i]
            list_of_tables.append(b)
        except:
            pass
    d = pd.DataFrame(list_of_tables)
    #alpha = (changing_date + ' F&O.csv')
    alpha = (str(x)+'d F&O.csv')
    d.to_csv(alpha)
    # return list_of_tables


# fo(okokok)

#d = pd.DataFrame(temp)
#alpha = (changing_date + ' F&O.csv')
# d.to_csv(alpha)


# for i in

# print(d)
# print('F&O from', final_url,
#      '\n\n\nEquity watch site : https://www1.nseindia.com/live_market/dynaContent/live_watch/equities_stock_watch.htm')
