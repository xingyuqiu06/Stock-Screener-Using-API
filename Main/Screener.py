import requests, time, re
import pandas as pd
import pickle as pkl
from key import api_key

print(time.asctime())

url = 'https://api.tdameritrade.com/v1/instruments' #https://developer.tdameritrade.com/instruments/apis/get/instruments

df = pd.read_csv('stock_list.csv')

symbols = [a.replace("^","-") for a in df['Symbol'].values]
print(symbols)
start = 0
end = 500

while start < len(symbols):
    tickers = symbols[start:end]

    payload = {'apikey':api_key,
               'symbol':tickers,
               'projection':'fundamental'}

    results = requests.get(url,params=payload)
    data = results.json()
    f_name = time.asctime()+'.pkl'
    f_name = re.sub('[ :]','_',f_name)
    with open(f_name,'wb') as file:
        pkl.dump(data,file)
    print(results.json())
    start = end
    end += 500
    time.sleep(1)