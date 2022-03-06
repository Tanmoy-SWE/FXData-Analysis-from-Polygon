import time
import requests
from sqlalchemy import create_engine

api_key = 'beBybSi8daPgsTp5yx5cHtHpYcrjp5Jq'

currency1 = 'CAD'
currency2 = 'AUD'
currency3 = 'EUR'
api_url_1 = 'https://api.polygon.io/v1/conversion/'+currency1+'/USD?amount=100&precision=2&apiKey='+api_key
api_url_2 = 'https://api.polygon.io/v1/conversion/'+currency2+'/USD?amount=100&precision=2&apiKey='+api_key
api_url_3 = 'https://api.polygon.io/v1/conversion/'+currency3+'/USD?amount=100&precision=2&apiKey='+api_key

#connection = create_engine('/Users/ahsanhabib/Desktop/FXData/FXData Analysis/mydb.sqlite')


usd_to_cad = requests.get(api_url_1).json()
usd_to_aud = requests.get(api_url_2).json()
usd_to_eur = requests.get(api_url_3).json()
print(usd_to_cad['last']['timestamp'])
print(usd_to_cad['last']['bid'])
timestamp_now = time.time()
print(timestamp_now)
timestamp_now = (int)(timestamp_now*1000)
print(timestamp_now)




