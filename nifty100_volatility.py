import daily_vol
import pandas as pd
import indices
import pdfkit
import subprocess
import tsend


def daily_volatility_pdf_send():
    daily_vol.get_file()
    df = pd.read_csv('Main.csv')
    df.rename(columns={'Underlying Close Price (A)': 'CP',
                       'Current Day Underlying Daily Volatility (E) = Sqrt(0.995*D*D + 0.005*C*C)': 'DV', 'Underlying Annualised Volatility (F) = E*Sqrt(365)': 'AV'}, inplace=True)
    df = df.set_index('Symbol')
    df.dropna(inplace=True)
    df.sort_values(by="DV", ascending=False, inplace=True)
    df = df.filter(items=['Symbol', 'Date', 'CP', 'DV', 'AV'])
    for i in df.index:
        if i not in indices.nifty100:
            df = df.drop([i])
    print(df)
    df.to_html('DV.html')
    pdfkit.from_file('DV.html', 'DV.pdf')
    tsend.send_file('DV.pdf')
    subprocess.call("rm -rf DV.html DV.pdf Main.csv", shell=True)
