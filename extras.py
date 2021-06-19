# import yfinance as yf
# msft = yf.Ticker("MSFT")
# print(msft)
# msft.info

#TORCH BUILTINS
# site : https://jovian.ml/aakashns/02-linear-regression

x = ['ACC', 'ADANIENT', 'ADANIPORTS', 'ADANIPOWER', 'AMARAJABAT', 'AMBUJACEM', 'APOLLOHOSP', 'APOLLOTYRE', 'ASHOKLEY',
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


import torch
import torch.nn as nn
import numpy as np

inputs = np.array([[209.2500, 215.4500, 203.9000],
                   [215.0000, 222.1000, 213.3000],
                   [217.1500, 221.5000, 216.3000],
                   [221.4000, 222.5500, 219.3000],
                   [220.2000, 226.9000, 219.5500],
                   [226.1500, 227.8500, 224.8500],
                   [227.8500, 231.5500, 224.2000],
                   [224.2500, 225.2000, 222.0500],
                   [222.6000, 226.3000, 222.2000],
                   [225.0000, 225.6500, 223.0000],
                   [223.8500, 223.9000, 222.1000],
                   [222.2500, 222.5000, 220.6500],
                   [221.4000, 223.4500, 221.3000],
                   [222.0000, 224.0000, 221.6500],
                   [223.8000, 224.7500, 222.2000],
                   [223.2000, 225.4000, 222.5500],
                   [225.0500, 225.9500, 223.0500],
                   [223.6500, 224.2500, 218.0000],
                   [219.4000, 219.9000, 216.7500],
                   [218.3500, 219.0000, 217.0000],
                   [218.1500, 218.7000, 214.7500],
                   [215.3500, 219.0000, 214.8500],
                   [218.0000, 218.4500, 215.7500],
                   [218.0500, 218.7500, 216.7500],
                   [217.6500, 223.2500, 217.2500]], dtype='float32')
targets = np.array([214.9000, 217.4500, 221.3000, 220.1000, 226.1000, 227.8500, 224.3500,
                    222.6500, 224.9500, 223.7500, 222.3500, 221.5000, 221.9500, 223.7000,
                    223.1500, 225.4000, 223.6500, 219.5000, 218.4500, 218.2500, 215.3500,
                    218.0000, 218.1500, 217.4000, 223.0500], dtype='float32')

inputs = torch.from_numpy(inputs)
targets = torch.from_numpy(targets)

from torch.utils.data import TensorDataset

# Define dataset
train_ds = TensorDataset(inputs, targets)
train_ds[0:5]

from torch.utils.data import DataLoader

# Define data loader
batch_size = 5
train_dl = DataLoader(train_ds, batch_size, shuffle=False)

# for xb, yb in train_dl:
#    print(xb)
#    print(yb)
#    break

# Define model
model = nn.Linear(25, 25)
print(model.weight)
print(model.bias)

# Parameters
# list(model.parameters())

# Generate predictions
# preds = model(inputs)
# preds

# Import nn.functional
import torch.nn.functional as F

# Define loss function
loss_fn = F.mse_loss

loss = loss_fn(model(inputs), model(targets))
print(loss)

# Define optimizer
opt = torch.optim.SGD(model.parameters(), lr=1e-8)


# Utility function to train the model
def fit(num_epochs, model, loss_fn, opt, train_dl):
    # Repeat for given number of epochs
    for epoch in range(num_epochs):

        # Train with batches of data
        for xb, yb in train_dl:
            # 1. Generate predictions
            pred = model(xb)

            # 2. Calculate loss
            loss = loss_fn(pred, yb)

            # 3. Compute gradients
            loss.backward()

            # 4. Update parameters using gradients
            opt.step()

            # 5. Reset the gradients to zero
            opt.zero_grad()

        # Print the progress
        if (epoch + 1) % 10 == 0:
            print('Epoch [{}/{}], Loss: {:.4f}'.format(epoch + 1, num_epochs, loss.item()))


fit(100, model, loss_fn, opt)

# Generate predictions
x1 = model(inputs)
print(x1)

print(targets)

"""""

### YAHOO QUERY


for i in range(2,len(df.index)):
    a = ((df.iloc[i-1])['Volume'])
    b = ((df.iloc[i])['Volume'])
    c = int(((b-a)/a)*100)
    d = str(df.index[i]) + ' vol change ibul : ' + str(c)+'%'+' ie. '+str(b-a)
    if ((c>=50) or (c<= -50)):
        tsend.send(d)


#df1 =df.iloc[0:-25]
df1['volume'].rolling(15).mean().plot()
#print(df1)









### CHECK PANDAS / CHECK PD.PY ###

import os

print(os.getcwd())
import pandas as pd

a = pd.read_csv("check.csv")
print(a.columns)
a.rename(columns={'Unnamed: 0':'Date'},inplace=True)
a.set_index('Date',inplace=True)
print(a.columns)

a.to_csv("final.csv")



#a = (a["open"],inplace=True)















import yfinace_import

data = yfinace_import.history(tickers='IBULHSGFIN.NS',period='30days',interval='1m')
print(data.head())

import yfinance as yf
import datetime
import pandas as pd

a = datetime.datetime.now()
data = yf.download(tickers='IBULHSGFIN.NS', start='2020-06-26', interval='15m')

print(a)
print(datetime.datetime.now())

d = pd.DataFrame(data)
alpha = ('Yfinance_ibul.csv')
d.to_csv(alpha)






###Yahoo query code###
from yahooquery import Ticker
import datetime
import pandas as pd

ibul = Ticker('IBULHSGFIN.NS')
a = datetime.datetime.now()
# d = pd.DataFrame(ibul.history(start='2020-06-23',interval='5m'))


d = pd.DataFrame(ibul.history(start='2020-06-26', interval='15m'))
print(a)
print(datetime.datetime.now())
alpha = ('Yquery_ibul.csv')
d.to_csv(alpha)

















### YAHOO QUERY ###

from yahooquery import Ticker
import datetime
import pandas as pd
import time

print(datetime.datetime.now())
ibul = Ticker('IBULHSGFIN.NS', formatted=True)

#a = datetime.datetime.now()

d = pd.DataFrame(ibul.history(start='2020-06-26', interval='15m'))
d.to_csv("ibul_26th_15m.csv")
a =pd.read_csv("ibul_26th_15m.csv")
a.rename(columns={'Unnamed: 0': 'Date'},inplace=True)
#time.sleep(2)
#d.set_index('Date', inplace=True)

for i in a:
    print(i)
#print(d)
# a = pd.read_csv("ibul_26th_15m.csv")
# print(a.columns)
# a.rename(columns={'Unnamed: 0':'Date'},inplace=True)
# a.set_index('Date',inplace=True)
# print(a.columns)
# a['Date'] = pd.to_datetime(a["Date"])
# a.to_csv("ibul_26th_15m.csv")

# for ind,row in a.iterrows():
#    print(row)


# ibul = pd.DataFrame(Ticker('IBULHSGFIN.NS',formatted=True).get_modules(["summaryDetail", "price"]))


# output_file = open('output.txt', 'w')
# output_file.write(str(ibul))
# output_file.close()










###   MULTITASKING   ######

# example.py
import multitasking
import time
import random
import signal

# kill all tasks on ctrl-c
#signal.signal(signal.SIGINT, multitasking.killall)

# or, wait for task to finish on ctrl-c:
# signal.signal(signal.SIGINT, multitasking.wait_for_tasks)

@multitasking.task # <== this is all it takes :-)
def hello(count):
    sleep = i
    print("Hello %s (sleeping for %ss)" % (count, sleep))
    time.sleep(sleep)
    print("Goodbye %s (after for %ss)" % (count, sleep))

if __name__ == "__main__":
    for i in range(0, 10):
        hello(i+1)
        print("middle"+str(i))
"""