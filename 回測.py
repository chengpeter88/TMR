import requests
import pandas as pd

# CoinMarketCap API根地址
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

# 设置头部参数,包括API Key
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'your_api_key' 
}

# GET请求获取实时数据
response = requests.get(url, headers=headers).json()

# 提取BTC/USD价格 ticker
btc_price = response['data']['1']['quote']['USD']['price'] 

# 放入Dataframe模拟新数据进入
df = pd.DataFrame(index=[df.index[-1]+pd.Timedelta(seconds=30)], columns=['Close'])  
df.loc[df.index[-1]] = [btc_price]

# 打印输出新数据
print(df)