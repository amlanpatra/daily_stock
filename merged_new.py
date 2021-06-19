import pandas as pd
import yfinance as yf
import tsend
import indices
import stock_ss

nifty101_to_200 = indices.nifty101_to_200
nifty_next50 = indices.nifty_next50
nifty50 = indices.nifty50
nifty_over200 = indices.nifty_over200


def trend(name_of_msg, index, ss_chart_duration='15', lmt=5):
    def ns(i):
        return i + '.NS'
    df = yf.download(tickers=list(map(ns, index)), period='4d', interval='1d')
    df = df.round(decimals=2)
    df_close = df['Close']
    df_vol = pd.DataFrame(df['Volume'])
    df_vol = df_vol.iloc[-1]
    df_vol.sort_values(inplace=True, ascending=False)
    ultimate_3nd_down = []
    ultimate_2nd_down = []
    ultimate_3nd_up = []
    ultimate_2nd_up = []
    for x in df_vol.index:
        try:
            df_new = df_close[x]
            day1 = df_new.iloc[0]
            day2 = df_new.iloc[1]
            day3 = df_new.iloc[2]
            day4 = df_new.iloc[3]
            change3 = round((day4 - day3), 2)
            change2 = round((day3 - day2), 2)
            change1 = round((day2 - day1), 2)
# downtrend
            if ((change3 < 0) and ((day4 > 100) and (day4 < 1000))):
                if (change2 < 0):
                    ultimate_2nd_down.append(x)
                    if (change1 < 0):
                        ultimate_3nd_down.append(x)
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
    try:
        for i in range(lmt):
            down2_str = down2_str + ',  ' + (ultimate_2nd_down[i])[:-3]
    except:
        pass
    try:
        for i in range(lmt):
            down3_str = down3_str + ',  ' + (ultimate_3nd_down[i])[:-3]
    except:
        pass
    try:
        for i in range(lmt):
            up2_str = up2_str + ',  ' + (ultimate_2nd_up[i])[:-3]
    except:
        pass
    try:
        for i in range(lmt):
            up3_str = up3_str + ',  ' + (ultimate_3nd_up[i])[:-3]
    except:
        pass

    down2_str = down2_str[1:]
    down3_str = down3_str[1:]
    up2_str = up2_str[1:]
    up3_str = up3_str[1:]

    tsend.start_dots(2, name_of_msg)
    tsend.send("2 days DOWN : {}".format(down2_str))
    tsend.send("3 days DOWN : {}".format(down3_str))
    tsend.send("2 days UP : {}".format(up2_str))
    tsend.send("3 days UP : {}".format(up3_str))

    final_list = [down2_str, down3_str, up2_str, up3_str]

    tsend.psend(name_of_msg)
    for i in range(4):
        for j in final_list[i]:
            stock_ss.send_stock_ss(j, ss_chart_duration)

    return final_list
