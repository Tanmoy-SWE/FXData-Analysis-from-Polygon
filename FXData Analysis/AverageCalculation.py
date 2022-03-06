from DatabaseCreation import dbms_usdToCAD, dbms_usdToCHF, dbms_usdToGBP, dbms_usdToEUR, dbms_usdToAUD
from DatabaseCreation import dbms_euroToUSD, dbms_audToUSD, dbms_gbpToUSD, dbms_chfToUSD, dbms_cadToUSD
import sqlite3

def show_average(databaseName, baseCurr, convertCurr):
    # Create a SQL connection to our SQLite database
    con = sqlite3.connect(databaseName)
    cur = con.cursor()
    # Return all results of query
    cur.execute('SELECT FXRate FROM fxdata')
    fxDataList = cur.fetchall()
    sum = 0
    for i in range(0,len(fxDataList)):
        sum = sum + fxDataList[i][0]
    #mean value
    mean = sum/len(fxDataList)
    print(f"Average Value of FXData ({baseCurr} to {convertCurr}):",mean)
    # Be sure to close the connection
    con.close()
    return mean

show_average('usdToCAD.sqlite', 'USD', 'CAD')
show_average('usdToAUD.sqlite', 'USD', 'AUD')
show_average('usdToEUR.sqlite', 'USD', 'EUR')
show_average('usdToGBP.sqlite', 'USD', 'GBP')
show_average('usdToCHF.sqlite', 'USD', 'CHF')
show_average('cadToUSD.sqlite', 'CAD', 'USD')
show_average('audToUSD.sqlite', 'AUD', 'USD')
show_average('euroToUSD.sqlite', 'EUR', 'USD')
show_average('gbpToUSD.sqlite', 'GBP', 'USD')
show_average('chfToUSD.sqlite', 'CHF', 'USD')