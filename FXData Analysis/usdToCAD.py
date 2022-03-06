import fxDatabase
import time
import requests
from DatabaseCreation import dbms_usdToCAD

api_key = 'beBybSi8daPgsTp5yx5cHtHpYcrjp5Jq'

currency1 = 'CAD'
api_url_1 = 'https://api.polygon.io/v1/conversion/' + currency1 + '/USD?amount=100&precision=2&apiKey=' + api_key
usd_to_cad = requests.get(api_url_1).json()
timestamp = usd_to_cad['last']['timestamp']
fxRate = usd_to_cad['last']['bid']
timestamp_now = time.time()
timestamp_now = (int)(timestamp_now * 1000)
print(timestamp_now)
query = f'Insert into FXData values(null, {timestamp}, {fxRate}, {timestamp_now})'
dbms_usdToCAD .execute_query(query)