import time
import requests
from DatabaseCreation import dbms_usdToCAD, dbms_usdToAUD, dbms_usdToEUR, dbms_usdToGBP, dbms_usdToCHF

api_key = 'beBybSi8daPgsTp5yx5cHtHpYcrjp5Jq'
curr = time.time()
onemin = curr + 86400
while(1):
    currency1 = 'CAD'
    api_url_1 = 'https://api.polygon.io/v1/conversion/' + currency1 + '/USD?amount=100&precision=2&apiKey=' + api_key
    usdToCurrency = requests.get(api_url_1).json()
    timestamp = usdToCurrency['last']['timestamp']
    fxRate =    usdToCurrency['last']['bid']
    timestamp_now = time.time()
    timestamp_now = (int)(timestamp_now)
    query = f'Insert into FXData values(null, {timestamp}, {fxRate}, {timestamp_now})'
    dbms_usdToCAD.execute_query(query)

    currency1 = 'AUD'
    api_url_1 = 'https://api.polygon.io/v1/conversion/' + currency1 + '/USD?amount=100&precision=2&apiKey=' + api_key
    usdToCurrency = requests.get(api_url_1).json()
    timestamp = usdToCurrency['last']['timestamp']
    fxRate =    usdToCurrency['last']['bid']
    timestamp_now = time.time()
    timestamp_now = (int)(timestamp_now)
    query = f'Insert into FXData values(null, {timestamp}, {fxRate}, {timestamp_now})'
    dbms_usdToAUD .execute_query(query)

    currency1 = 'EUR'
    api_url_1 = 'https://api.polygon.io/v1/conversion/' + currency1 + '/USD?amount=100&precision=2&apiKey=' + api_key
    usdToCurrency = requests.get(api_url_1).json()
    timestamp = usdToCurrency['last']['timestamp']
    fxRate =    usdToCurrency['last']['bid']
    timestamp_now = time.time()
    timestamp_now = (int)(timestamp_now)
    query = f'Insert into FXData values(null, {timestamp}, {fxRate}, {timestamp_now})'
    dbms_usdToEUR.execute_query(query)

    currency1 = 'GBP'
    api_url_1 = 'https://api.polygon.io/v1/conversion/' + currency1 + '/USD?amount=100&precision=2&apiKey=' + api_key
    usdToCurrency = requests.get(api_url_1).json()
    timestamp = usdToCurrency['last']['timestamp']
    fxRate =    usdToCurrency['last']['bid']
    timestamp_now = time.time()
    timestamp_now = (int)(timestamp_now)
    query = f'Insert into FXData values(null, {timestamp}, {fxRate}, {timestamp_now})'
    dbms_usdToGBP.execute_query(query)

    currency1 = 'CHF'
    api_url_1 = 'https://api.polygon.io/v1/conversion/' + currency1 + '/USD?amount=100&precision=2&apiKey=' + api_key
    usdToCurrency = requests.get(api_url_1).json()
    timestamp = usdToCurrency['last']['timestamp']
    fxRate =    usdToCurrency['last']['bid']
    timestamp_now = time.time()
    timestamp_now = (int)(timestamp_now)
    query = f'Insert into FXData values(null, {timestamp}, {fxRate}, {timestamp_now})'
    dbms_usdToCHF.execute_query(query)


