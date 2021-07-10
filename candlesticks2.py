import pandas as pd
import yfinance as yf
import tsend


def get_df(indices, intrvl='1d', perd='1d', quantity=0, add_ns=1):
    def ns(x):
        return x + '.NS'
    if add_ns == 0:
        df = yf.download(tickers=indices,
                         period=perd, interval=intrvl)
    else:
        df = yf.download(tickers=list(map(ns, indices)),
                         period=perd, interval=intrvl)
    df = df.dropna()
    df = df.iloc[-1] if perd == '1d' else df
    df = pd.DataFrame(df[["Open", "High", "Low", "Close"]])
    df = df.round(decimals=2)
    return df


def ohlc_df(origin_df):
    arr = []
    origin_df = origin_df.T
    for i in origin_df['Open']:
        arr.append(i)
    destination_df = pd.DataFrame(arr, columns=['Name'])
    destination_df.set_index('Name', inplace=True)
    for i in ['Open', 'High', 'Low', 'Close']:
        arr = []
        for j in origin_df.iloc[-1][i]:
            arr.append(j)
        destination_df[i] = arr
    return destination_df


# g = '' FIXME: fix g


def regex(df, quantity, file_name):
    idx = list(df.index)
    for i in range(len(idx)):
        idx[i] = idx[i].replace('&', '_') if '&' in idx[i] else idx[i]
        idx[i] = idx[i].replace('-', '_') if '-' in idx[i] else idx[i]
        idx[i] = idx[i].replace('.NS', '') if '.NS' in idx[i] else idx[i]
        while(len(idx[i]) != 20):
            idx[i] += '_'
    df.index = idx
    if quantity != 0:
        df = df.head(quantity)
    upload_lst = ''
    for i in df.index:
        if '_' in i:
            j = i.replace('_', '')
            j += ','
        upload_lst += j
    f = open("/Users/amlanpatra/Desktop/stk_test/{}.txt".format(file_name), "w")
    f.write(upload_lst)
    f.close()
    # global g  FIXME: global g must be fixed so that all values can be accessed in 1 file ie mix.txt
    # g += upload_lst
    return df


def candlesticks(indices, intrvl='1d', perd='1d', quantity=0, add_ns=1):
    # g = '' FIXME: fix g
    df = ohlc_df(get_df(indices, intrvl, perd, quantity, add_ns))

    def most_change(df):
        temp = ((abs(df['Close'] - df['Open']))*100) / df['Open']
        df['Change%'] = temp
        df = pd.DataFrame(df.sort_values(by=['Change%'], ascending=False))
        df = df[['Change%']]
        df = regex(df, quantity, 'most_change')
        return str(df)  # TODO: typecasts df to string

    def doji(df):
        temp = ((abs(df['Close'] - df['Open']))*100) / (df['High'] - df['Low'])
        temp = round(temp, 2)
        df['Doji'] = temp
        df = pd.DataFrame(df.sort_values(by=['Doji'], ascending=True))
        df = df[['Change%']]
        df = regex(df, quantity, 'doji')
        # TODO: typecasts df to string
        return 'No Candle forming Doji' if df.empty else str(df)


# high - close <= 10% of [high-low] : also to be sorted in this order : ascending
# close - open >= 0
# open - mid >= 0

    def hammer(df):
        mid = round((df['High'] + df['Low'])/2, 2)
        df['Mid'] = mid
        high_low = df['High'] - df['Low']
        high_low_1pc = high_low/100
        df['High_close'] = df['High'] - df['Close']
        df = df.loc[(df['High_close'] <= 10 * high_low_1pc)]
        df = df.loc[(df['Close']-df['Open'] > 0) &
                    (df['Open'] - df['Mid'] >= 0)]
        df = df[['High_close']]
        df = regex(df, quantity, 'hammer')
        return 'No Candle forming hammer' if df.empty else str(df)

    # f = open("/Users/amlanpatra/Desktop/stk_test/mix.txt", "w")
    # f.write(g)
    # f.close() FIXME:fix g and put value to mix.txt file
    tsend.test_send("Most change : {}".format(most_change(df)))
    tsend.test_send("Doji : {}".format(doji(df)))
    tsend.test_send("Hammer : {}".format(hammer(df)))
