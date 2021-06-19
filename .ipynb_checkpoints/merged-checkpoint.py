import pandas as pd
import yfinance as yf
import tsend
import indices
indices = indices.indices

# todo : 1. send 2nd and 3rd according to volume
# instead of separately sending for volume

# sort dataframe in descending order
# df.sort_values(by=['Brand'], inplace=True, ascending=False)


def trend():
    per = '4d'
    ultimate_3nd_down = []
    ultimate_2nd_down = []
    ultimate_3nd_up = []
    ultimate_2nd_up = []

    for x in indices:
        b = x+'.NS'
        print(b)
        data = yf.download(tickers=b, period=per, interval='1d')
        df = pd.DataFrame(data)
        df = df.round(decimals=2)

        try:
            day1 = df.iloc[0]['Close']
            day2 = df.iloc[1]['Close']
            day3 = df.iloc[2]['Close']
            day4 = df.iloc[3]['Close']
            change3 = round((day4 - day3), 2)
            change2 = round((day3 - day2), 2)
            change1 = round((day2 - day1), 2)


# downtrend
            if ((change3 < 0) and ((day4 > 100) and (day4 < 1000))):
                if (change2 < 0):
                    ultimate_2nd_down.append(x)
                    if (change1 < 0):
                        ultimate_3nd_down.append(x)
                        print(x)

# uptrend
            if ((change3 > 0) and ((day4 > 100) and (day4 < 1000))):
                if (change2 > 0):
                    ultimate_2nd_up.append(x)
                    if (change1 > 0):
                        ultimate_3nd_up.append(x)

        except:
            pass

    for i in ultimate_3nd_down:
        ultimate_2nd_down.remove(i)

    for i in ultimate_3nd_up:
        ultimate_2nd_up.remove(i)

    down2_str = ''
    down3_str = ''
    up2_str = ''
    up3_str = ''

    for i in ultimate_2nd_down:
        down2_str = i + ',' + down2_str
    down2_str = down2_str[:-1]

    for i in ultimate_3nd_down:
        down3_str = i + ',' + down3_str
    down3_str = down3_str[:-1]

    for i in ultimate_2nd_up:
        up2_str = i + ',' + up2_str
    up2_str = up2_str[:-1]

    for i in ultimate_3nd_up:
        up3_str = i + ',' + up3_str
    up3_str = up3_str[:-1]

    tsend.start_dots(1, "2 days DOWN")
    tsend.send(down2_str)
    tsend.start_dots(1, "3 days DOWN")
    tsend.send(down3_str)
    tsend.start_dots(1, "2 days UP")
    tsend.send(up2_str)
    tsend.start_dots(1, "3 days UP")
    tsend.send(up3_str)


trend()
