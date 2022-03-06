from DatabaseCreation import dbms_usdToCAD, dbms_usdToCHF, dbms_usdToGBP, dbms_usdToEUR, dbms_usdToAUD
from DatabaseCreation import dbms_euroToUSD, dbms_audToUSD, dbms_gbpToUSD, dbms_chfToUSD, dbms_cadToUSD
import sqlite3
import statistics

def show_average_6_mins(databaseName, currFrom, currTo):
    con = sqlite3.connect(databaseName)
    cur = con.cursor()
    cur.execute('SELECT EntryTime FROM fxdata')
    DList = cur.fetchall()
    listlen = len(DList)
    last = (int)(DList[listlen-1][0])
    first = (int)(DList[0][0])
    for i in range(first,last, 360):
        con = sqlite3.connect(databaseName)
        cur = con.cursor()
        cur.execute('SELECT EntryTime FROM fxdata')
        DataList = cur.fetchall()
        ent = (int)(first) + 360
        cur = con.cursor()
        cur.execute('SELECT FXRate FROM fxdata WHERE EntryTime Between '+ (str)(i) + ' AND ' + (str)(i+360))
        fDataList = cur.fetchall()
        sum = 0
        for j in range(0,len(fDataList)):
            sum = sum + fDataList[j][0]
        if len(fDataList)!= 0:
            mean = sum / len(fDataList)
            print(f"6 mins Average Value of FXData ({currFrom} to {currTo}):",mean)
        else:
            print(f"6 mins Average Value of FXData ({currFrom} to {currTo}):",mean)

def show_std_6_mins(databaseName, currFrom, currTo):
    con = sqlite3.connect(databaseName)
    cur = con.cursor()
    cur.execute('SELECT EntryTime FROM fxdata')
    DList = cur.fetchall()
    listlen = len(DList)
    last = (int)(DList[listlen-1][0])
    first = (int)(DList[0][0])
    for i in range(first,last, 360):
        con = sqlite3.connect(databaseName)
        cur = con.cursor()
        cur.execute('SELECT EntryTime FROM fxdata')
        DataList = cur.fetchall()
        ent = (int)(first) + 360
        cur = con.cursor()
        cur.execute('SELECT FXRate FROM fxdata WHERE EntryTime Between '+ (str)(i) + ' AND ' + (str)(i+360))
        fDataList = cur.fetchall()
        list1 = [0,0]
        for ele in range(0,len(fDataList)):
            list1.append((int)(fDataList[ele][0]))
        std = statistics.stdev(list1)
        print(f"6 mins STD Value of FXData ({currFrom} to {currTo}):",std)

def show_std_1hr(databaseName, currFrom, currTo):
    con = sqlite3.connect(databaseName)
    cur = con.cursor()
    cur.execute('SELECT EntryTime FROM fxdata')
    DList = cur.fetchall()
    listlen = len(DList)
    last = (int)(DList[listlen-1][0])
    first = (int)(DList[0][0])
    stds = [0,0]
    for i in range(first,last, 360):
        con = sqlite3.connect(databaseName)
        cur = con.cursor()
        cur.execute('SELECT EntryTime FROM fxdata')
        DataList = cur.fetchall()
        ent = (int)(first) + 360
        cur = con.cursor()
        cur.execute('SELECT FXRate FROM fxdata WHERE EntryTime Between '+ (str)(i) + ' AND ' + (str)(i+360))
        fDataList = cur.fetchall()
        list1 = [0,0]
        for ele in range(0,len(fDataList)):
            list1.append((int)(fDataList[ele][0]))
        std = statistics.stdev(list1)
        stds.append(std)
    print(f"1 hr Maximum STD Value of FXData ({currFrom} to {currTo}):",max(stds))
    print(f"1 hr Minimum STD Value of FXData ({currFrom} to {currTo}):",min(stds))

show_average_6_mins('usdToCAD.sqlite', 'USD', 'CAD')
show_average_6_mins('usdToAUD.sqlite', 'USD', 'AUD')
show_average_6_mins('usdToEUR.sqlite', 'USD', 'EUR')
show_average_6_mins('usdToGBP.sqlite', 'USD', 'GBP')
show_average_6_mins('usdToCHF.sqlite', 'USD', 'CHF')
show_average_6_mins('cadToUSD.sqlite', 'CAD', 'USD')
show_average_6_mins('audToUSD.sqlite', 'AUD', 'USD')
show_average_6_mins('euroToUSD.sqlite', 'EUR', 'USD')
show_average_6_mins('gbpToUSD.sqlite', 'GBP', 'USD')
show_average_6_mins('chfToUSD.sqlite', 'CHF', 'USD')

show_std_6_mins('usdToCAD.sqlite', 'USD', 'CAD')
show_std_6_mins('usdToAUD.sqlite', 'USD', 'AUD')
show_std_6_mins('usdToEUR.sqlite', 'USD', 'EUR')
show_std_6_mins('usdToGBP.sqlite', 'USD', 'GBP')
show_std_6_mins('usdToCHF.sqlite', 'USD', 'CHF')
show_std_6_mins('cadToUSD.sqlite', 'CAD', 'USD')
show_std_6_mins('audToUSD.sqlite', 'AUD', 'USD')
show_std_6_mins('euroToUSD.sqlite', 'EUR', 'USD')
show_std_6_mins('gbpToUSD.sqlite', 'GBP', 'USD')
show_std_6_mins('chfToUSD.sqlite', 'CHF', 'USD')

show_std_1hr('usdToCAD.sqlite', 'USD', 'CAD')
show_std_1hr('usdToAUD.sqlite', 'USD', 'AUD')
show_std_1hr('usdToEUR.sqlite', 'USD', 'EUR')
show_std_1hr('usdToGBP.sqlite', 'USD', 'GBP')
show_std_1hr('usdToCHF.sqlite', 'USD', 'CHF')
show_std_1hr('cadToUSD.sqlite', 'CAD', 'USD')
show_std_1hr('audToUSD.sqlite', 'AUD', 'USD')
show_std_1hr('euroToUSD.sqlite', 'EUR', 'USD')
show_std_1hr('gbpToUSD.sqlite', 'GBP', 'USD')
show_std_1hr('chfToUSD.sqlite', 'CHF', 'USD')