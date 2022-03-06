import sqlite3
import matplotlib.pyplot as plt

class CurrencyPair:
    def __init__(self,currency1, currency2):
        self.currency1 = currency1
        self.currency2 = currency2
        api_key = 'beBybSi8daPgsTp5yx5cHtHpYcrjp5Jq'
        api_url_1 = 'https://api.polygon.io/v1/conversion/' + self.currency1 + '/'+self.currency2+'?amount=100&precision=2&apiKey=' + api_key

    def saveToList(self, databaseName, list1):
        # Create a SQL connection to our SQLite database
        con = sqlite3.connect(databaseName)
        cur = con.cursor()
        # Return all results of query
        cur.execute('SELECT FXRate FROM fxdata')
        fxDataList = cur.fetchall()
        list2 = []
        oldest_data = fxDataList[0][0]
        for i in range(0, len(fxDataList)):
            historical_return = (fxDataList[i][0] - oldest_data)/oldest_data
            #converting to percentage
            historical_return = historical_return * 100
            list1.append(historical_return)
        con.close()


historicalValues = CurrencyPair('USD','CAD')
usdToCAD = []

historicalValues.saveToList('usdToCAD.sqlite',usdToCAD)
print(usdToCAD)


historicalValues = CurrencyPair('USD','AUD')
usdToAUD = []

historicalValues.saveToList('usdToAUD.sqlite',usdToAUD)
print(usdToAUD)

historicalValues = CurrencyPair('USD','EUR')
usdToEUR = []

historicalValues.saveToList('usdToEUR.sqlite',usdToEUR)
print(usdToEUR)


historicalValues = CurrencyPair('USD','CHF')
usdToCHF = []

historicalValues.saveToList('usdToCHF.sqlite',usdToCHF)
print(usdToCHF)

historicalValues = CurrencyPair('USD','GBP')
usdToGBP = []

historicalValues.saveToList('usdToGBP.sqlite',usdToGBP)
print(usdToGBP)

historicalValues = CurrencyPair('EUR','USD')
eurToUSD = []

historicalValues.saveToList('eurToUSD.sqlite',eurToUSD)
print(eurToUSD)

historicalValues = CurrencyPair('CAD','USD')
cadToUSD = []

historicalValues.saveToList('cadToUSD.sqlite',cadToUSD)
print(cadToUSD)

historicalValues = CurrencyPair('AUD','USD')
audToUSD = []

historicalValues.saveToList('audToUSD.sqlite',audToUSD)
print(audToUSD)

historicalValues = CurrencyPair('CHF','USD')
chfToUSD = []

historicalValues.saveToList('chfToUSD.sqlite',chfToUSD)
print(chfToUSD)

historicalValues = CurrencyPair('GBP','USD')
gbpToUSD = []

historicalValues.saveToList('gbpToUSD.sqlite',gbpToUSD)
print(gbpToUSD)

#Plotting the histogram of the historical Returns
plt.hist(usdToCAD, edgecolor = 'black')
plt.xlabel('time')
plt.ylabel('Historical Return')
plt.title("USD To CAD")
plt.show()

plt.hist(usdToAUD, edgecolor = 'black')
plt.xlabel('time')
plt.ylabel('Historical Return')
plt.title("USD To AUD")
plt.show()

plt.hist(usdToEUR, edgecolor = 'black')
plt.xlabel('time')
plt.ylabel('Historical Return')
plt.title("USD To EUR")
plt.show()

plt.hist(usdToCHF, edgecolor = 'black')
plt.xlabel('time')
plt.ylabel('Historical Return')
plt.title("USD To CHF")
plt.show()

plt.hist(usdToGBP, edgecolor = 'black')
plt.xlabel('time')
plt.ylabel('Historical Return')
plt.title("USD To GBP")
plt.show()

plt.hist(cadToUSD, edgecolor = 'black')
plt.xlabel('time')
plt.ylabel('Historical Return')
plt.show()

plt.hist(audToUSD, edgecolor = 'black')
plt.xlabel('time')
plt.ylabel('Historical Return')
plt.show()

plt.hist(eurToUSD, edgecolor = 'black')
plt.xlabel('time')
plt.ylabel('Historical Return')
plt.show()

plt.hist(chfToUSD, edgecolor = 'black')
plt.xlabel('time')
plt.ylabel('Historical Return')
plt.show()

plt.hist(gbpToUSD, edgecolor = 'black')
plt.xlabel('time')
plt.ylabel('Historical Return')
plt.show()