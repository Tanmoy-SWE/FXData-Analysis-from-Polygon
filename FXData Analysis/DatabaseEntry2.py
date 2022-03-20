from DatabaseCreation import dbms_cadToUSD, dbms_chfToUSD, dbms_gbpToUSD, dbms_euroToUSD, dbms_audToUSD
import sqlite3

# Create a SQL connection to our SQLite database
con = sqlite3.connect("usdToCAD.sqlite")
cur = con.cursor()
# Return all results of query
cur.execute('SELECT * FROM fxdata')
fxDataList = cur.fetchall()
for i in range(0, len(fxDataList)):
    query = f'Insert into FXData values(null, {fxDataList[i][1]}, {1/fxDataList[i][2]}, {fxDataList[i][3]})'
    dbms_cadToUSD.execute_query(query)
con.close()

con = sqlite3.connect("usdToCHF.sqlite")
cur = con.cursor()
# Return all results of query
cur.execute('SELECT * FROM fxdata')
fxDataList = cur.fetchall()
for i in range(0, len(fxDataList)):
    query = f'Insert into FXData values(null, {fxDataList[i][1]}, {1/fxDataList[i][2]}, {fxDataList[i][3]})'
    dbms_chfToUSD.execute_query(query)
con.close()

con = sqlite3.connect("usdToAUD.sqlite")
cur = con.cursor()
# Return all results of query
cur.execute('SELECT * FROM fxdata')
fxDataList = cur.fetchall()
for i in range(0, len(fxDataList)):
    query = f'Insert into FXData values(null, {fxDataList[i][1]}, {1/fxDataList[i][2]}, {fxDataList[i][3]})'
    dbms_audToUSD.execute_query(query)
con.close()

con = sqlite3.connect("usdToGBP.sqlite")
cur = con.cursor()
# Return all results of query
cur.execute('SELECT * FROM fxdata')
fxDataList = cur.fetchall()
for i in range(0, len(fxDataList)):
    query = f'Insert into FXData values(null, {fxDataList[i][1]}, {1/fxDataList[i][2]}, {fxDataList[i][3]})'
    dbms_gbpToUSD.execute_query(query)
con.close()

con = sqlite3.connect("usdToEUR.sqlite")
cur = con.cursor()
# Return all results of query
cur.execute('SELECT * FROM fxdata')
fxDataList = cur.fetchall()
for i in range(0, len(fxDataList)):
    query = f'Insert into FXData values(null, {fxDataList[i][1]}, {1/fxDataList[i][2]}, {fxDataList[i][3]})'
    dbms_euroToUSD.execute_query(query)
con.close()