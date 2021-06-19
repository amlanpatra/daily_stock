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
    # print(df2)
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

    #temp = ((df2['High'] - df2['Low'])*100) / df2['Average']
    temp = ((df2['Close'] - df2['Open'])*100) / df2['Open']
    df2['Change%'] = temp

    temp = (df2['Close']-df2['Open'])
    df2['Diff'] = temp

    final_df = pd.DataFrame(df2.sort_values(
        by=['Change%'], ascending=False))

    print(final_df)
    # if add_ns == 0:
    final_df = final_df[['Change%']]

    idx = list(final_df.index)
    for i in range(len(idx)):
        try:
            idx[i] = idx[i].replace('&', '_')
        except:
            pass

        try:
            idx[i] = idx[i].replace('.NS', '')
            while(len(idx[i]) != 20):
                idx[i] += '_'

        except:
            pass

    final_df.index = idx
    if quantity != 0:
        final_df = final_df.head(quantity)

    upload_lst = ''
    for i in final_df.index:
        if '_' in i:
            j = i.replace('_', '')
            j += ','
        upload_lst += j

    f = open("/Users/amlanpatra/Desktop/stk/change.txt", "w")
    f.write(upload_lst)
    f.close()

    return final_df

    """   
    
    

                if add_ns != 0:
                idx[i] = idx[i].replace('.NS', '    ')
            else:
    
    
        a = ''

    if add_ns == 0:
        pos = 'Positive : '
        neg = '\n Negative : '
        for i in range(len(final_df.index)):
            if(final_df.iloc[i]['Diff'] > 0):
                pos += (final_df.index[i]) + ',  '
            else:
                neg += (final_df.index[i]) + ',  '

        pos = pos[:-3]
        neg = neg[:-3]
        a = pos + ' \n ' + neg + ' \n\n '
    
    
    
    if quantity == 0:
         for i in final_df.index:
             # print(i)
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
             # print(j)
             if '&' in j:
                 j = j.replace('&', '_')
             a += ',  '+j
         a = a[3:]
         """
