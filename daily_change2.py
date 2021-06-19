import indices
import tsend
import yfinance as yf
import pandas as pd


def max_daily_change(indices, intrvl='1d', quantity=0, add_ns=1):
    def ns(x):
        return x+'.NS'
    if add_ns == 0:
        df = yf.download(tickers=indices, period='1d', interval=intrvl)
    else:
        df = yf.download(tickers=list(map(ns, indices)),
                         period='1d', interval=intrvl)
    df = df.dropna()
    df = df.iloc[-1]
    df = pd.DataFrame(df[["Open", "High", "Low", "Close"]])
    df = df.round(decimals=2)

    # print(df.index)
    df = df.T
    arr = []
    for i in df['Open']:
        arr.append(i)
    df2 = pd.DataFrame(arr, columns=['Name'])
    df2.set_index('Name', inplace=True)
    # display(df2)
    arr = []
    for i in df.iloc[-1]['Open']:
        arr.append(i)
    df2['Open'] = arr
    arr = []
    for i in df.iloc[-1]['High']:
        arr.append(i)
    df2['High'] = arr
    arr = []
    for i in df.iloc[-1]['Low']:
        arr.append(i)
    df2['Low'] = arr
    arr = []
    for i in df.iloc[-1]['Close']:
        arr.append(i)
    df2['Close'] = arr
    temp = (df2['High'] + df2['Low'])/2
    df2['Average'] = temp
    temp = ((df2['High'] - df2['Low'])*100) / df2['Average']
    df2['InDay%Change'] = temp
    final_df = df2.sort_values(by=['InDay%Change'], ascending=False)
    a = ''

    if quantity == 0:
        for i in final_df.index:
            print(i[:-3])
            if '&' in i:
                i = i.replace('&', '_')
            if add_ns == 0:
                a += ' \n  '+i
            else:
                a += ' \n  '+i[:-3]
        a = a[3:] if add_ns == 1 else a

    else:
        for i in range(quantity):
            j = (final_df.index[i])[:-3]
            print(j)
            if '&' in j:
                j = j.replace('&', '_')
            a += ',  '+j
        a = a[3:]

    return a
