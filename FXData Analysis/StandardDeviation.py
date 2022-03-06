import statistics

from DatabaseCreation import dbms_usdToCAD, dbms_usdToCHF, dbms_usdToGBP, dbms_usdToEUR, dbms_usdToAUD
from DatabaseCreation import dbms_euroToUSD, dbms_audToUSD, dbms_gbpToUSD, dbms_chfToUSD, dbms_cadToUSD
import sqlite3
from AverageCalculation import show_average
import math

def std(databaseName, baseCurr, convertCurr):
    # Create a SQL connection to our SQLite database
    con = sqlite3.connect(databaseName)
    cur = con.cursor()
    # Return all results of query
    cur.execute('SELECT FXRate FROM fxdata')
    fDataList = cur.fetchall()
    list1 = [0, 0]
    for ele in range(0, len(fDataList)):
        list1.append((int)(fDataList[ele][0]))
    std = statistics.stdev(list1)
    print(f"Standard Deviation of FXData ({baseCurr} to {convertCurr}):",std)
    # Be sure to close the connection
    con.close()
    return std

std('usdToCAD.sqlite', 'USD', 'CAD')
std('usdToAUD.sqlite', 'USD', 'AUD')
std('usdToEUR.sqlite', 'USD', 'EUR')
std('usdToGBP.sqlite', 'USD', 'GBP')
std('usdToCHF.sqlite', 'USD', 'CHF')
std('cadToUSD.sqlite', 'CAD', 'USD')
std('audToUSD.sqlite', 'AUD', 'USD')
std('euroToUSD.sqlite', 'EUR', 'USD')
std('gbpToUSD.sqlite', 'GBP', 'USD')
std('chfToUSD.sqlite', 'CHF', 'USD')