import pandas as pd
import yfinance as yf


def candlesticks(indices, intrvl='1d', perd='1d', quantity=0, add_ns=1):
        def ns(x):
            return x + '.NS'

        if add_ns == 0:
            df = yf.download(tickers=indices,period=perd, interval=intrvl)
        else:
            df = yf.download(tickers=list(map(ns, indices)),period=perd, interval=intrvl)

        df = df.dropna()
        df = df.iloc[-1] if perd == '1d' else df
        df = pd.DataFrame(df[["Open", "High", "Low", "Close"]])
        df = df.round(decimals=2)



def add_column(origin_df, destination_df, col_name):
    arr = []
    for i in origin_df.iloc[-1][col_name]:
        arr.append(i)
    destination_df = pd.DataFrame(destination_df)
    return destination_df

def doji(indices, intrvl='1d', quantity=0, add_ns=1):
        df = df
        df = df.T
        # print(df.index)

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

        # temp = ((df2['High'] - df2['Low'])*100) / df2['Average']
        temp = ((df2['Close'] - df2['Open'])*100) / df2['Open']
        df2['Change%'] = temp

        temp = (df2['Close']-df2['Open'])
        df2['Diff'] = temp

        temp = ((abs(df2['Close'] - df2['Open']))*100) / \
            (df2['High'] - df2['Low'])
        temp = round(temp, 2)
        df2['Doji'] = temp

        final_df = pd.DataFrame(df2.sort_values(
            by=['Doji'], ascending=True))
        print(final_df)
        # if add_ns == 0:
        final_df = final_df[['Doji']]
        counter = 0
        idx = list(final_df.index)
        for i in range(len(idx)):
            if (final_df.iloc[i]['Doji'] <= 20):
                counter += 1
                try:
                    idx[i] = idx[i].replace('&', '_')
                except:
                    pass

                try:
                    idx[i] = idx[i].replace('.NS', '')
                    while(len(idx[i]) != 18):
                        idx[i] += '_'

                except:
                    pass

        final_df.index = idx
        if quantity != 0:
            try:
                final_df = final_df.head(
                    quantity) if counter > quantity else final_df.head(counter)
            except:
                final_df = final_df.head()

        upload_lst = ''
        for i in final_df.index:
            if '_' in i:
                j = i.replace('_', '')
                j += ','
            upload_lst += j

        f = open("/Users/amlanpatra/Desktop/stk/doji.txt", "w")
        f.write(upload_lst)
        f.close()

        return final_df
