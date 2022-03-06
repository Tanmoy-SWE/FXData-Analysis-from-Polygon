from .CurrencyPair import CurrencyPair

historicalValues = CurrencyPair('USD','CAD')
list1 = []

historicalValues.saveToList('usdToCAD.sqlite',list1)
print(list1)