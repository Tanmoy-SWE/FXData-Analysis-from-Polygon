import sqlite3

# Create a SQL connection to our SQLite database
con = sqlite3.connect("usdToAUD.sqlite")
cur = con.cursor()
# Return all results of query
cur.execute('SELECT FXRate FROM fxdata')
fxDataList = cur.fetchall()
sum = 0
for i in range(0,len(fxDataList)):
    sum = sum + fxDataList[i][0]
#mean value
mean = sum/len(fxDataList)
print("Mean Value of FXData (USD to AUD):",mean)
# Be sure to close the connection
con.close()