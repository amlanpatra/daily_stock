import indices
import pandas as pd
import yfinance as yf


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


def regex(df, quantity, file_name):
    idx = list(df.index)
    for i in range(len(idx)):
        idx[i] = idx[i].replace('&', '_') if '&' in idx[i] else idx[i]
        idx[i] = idx[i].replace('.NS', '') if '.NS' in idx[i] else idx[i]
        idx[i] = idx[i].replace('-', '_') if '-' in idx[i] else idx[i]
        while(len(idx[i]) != 20):
            idx[i] += '_'
    df.index = idx
    # print("df is ", df)  # FIXME: remove this
    if quantity != 0:
        try:
            df = df.head(quantity)
        except:
            pass
    upload_lst = ''
    for i in df.index:
        j = i
        while(j[-1] == '_'):
            j = j[:-1]
        upload_lst = upload_lst + j + ','
    f = open("/Users/amlanpatra/Desktop/stk_test/{}.txt".format(file_name), "w")
    f.write(upload_lst)
    f.close()
    f = open("/Users/amlanpatra/Desktop/stk_test/mix.txt", 'a')
    f.write(upload_lst)
    f.close()
    return df


def range_bound_close(df, price_range_below=0, price_range_above=0):
    if not (price_range_below == 0 and price_range_above == 0):
        # df = df.loc[(df['Close'] > price_range_below and df['Close']
        #              < price_range_above)]
        df = df.loc[(df['Close'] >= price_range_below) &
                    (df['Close'] <= price_range_above)]
    return df


class candlesticks:

    def __init__(self, indices, intrvl='1d', perd='1d', quantity=0, add_ns=1):
        self.indices = indices
        self.intrvl = intrvl
        self.perd = perd
        self.quantity = quantity
        self.add_ns = add_ns
        # self.price_range_below = price_range_below
        # self.price_range_above = price_range_above
        self.df = ohlc_df(get_df(self.indices, self.intrvl,
                                 self.perd, self.quantity, self.add_ns))
        f = open("/Users/amlanpatra/Desktop/stk_test/mix.txt", 'w')
        f.write('')
        f.close()
        # FIXME: below is to print the df with which operations will begin
        print(self.df)

    def most_change(self, price_range_below=0, price_range_above=0):
        df = self.df
        temp = round(((abs(df['Close'] - df['Open']))*100) / df['Open'], 2)
        df['Change%'] = temp
        df = pd.DataFrame(df.sort_values(by=['Change%'], ascending=False))
        df = range_bound_close(df, price_range_below, price_range_above)
        print(df)  # FIXME: print this to find out the full df before deleting columns
        df = df[['Change%']]
        df = regex(df, self.quantity, 'most_change')
        return str(df)  # NOTE: typecasts df to string

    def doji(self, price_range_below=0, price_range_above=0):
        df = self.df
        temp = ((abs(df['Close'] - df['Open']))*100) / (df['High'] - df['Low'])
        temp = round(temp, 2)
        df['Doji'] = temp
        df = pd.DataFrame(df.sort_values(by=['Doji'], ascending=True))
        df = range_bound_close(df, price_range_below, price_range_above)
        df = df[['Doji']]
        df = regex(df, self.quantity, 'doji')   # NOTE: typecasts df to string
        return 'No Candle forming Doji' if df.empty else str(df)

    # Below Hammer logic
    # high - close <= 10% of [high-low] : also to be sorted in this order : ascending
    # close - open >= 0
    # open - mid >= 0

    def hammer(self, price_range_below=0, price_range_above=0):
        df = self.df
        mid = round((df['High'] + df['Low'])/2, 2)
        df['Mid'] = mid
        high_low = df['High'] - df['Low']
        high_low_1pc = high_low/100
        df['High_close'] = df['High'] - df['Close']
        df = df.loc[(df['High_close'] <= 10 * high_low_1pc)]
        df = df.loc[(df['Close']-df['Open'] > 0) &
                    (df['Open'] - df['Mid'] >= 0)]
        df = range_bound_close(df, price_range_below, price_range_above)
        df = df[['High_close']]
        df = regex(df, self.quantity, 'hammer')
        return 'No Candle forming hammer' if df.empty else str(df)


# a = candlesticks(indices.nifty50, '5m', quantity=5)
# print(format(a.most_change(300, 1500)))
# # print(format(a.most_change()))
# del a
