import fxDatabase
import time
import requests
from sqlalchemy import create_engine
from sqlalchemy import insert

dbms_usdToCAD = fxDatabase.FXDatabase(fxDatabase.SQLITE, dbname = 'usdToCAD.sqlite')
dbms_usdToCAD .create_db_tables()
dbms_usdToCAD .print_all_data()


dbms_usdToAUD = fxDatabase.FXDatabase(fxDatabase.SQLITE, dbname = 'usdToAUD.sqlite')
dbms_usdToAUD .create_db_tables()
dbms_usdToAUD .print_all_data()


dbms_usdToEUR = fxDatabase.FXDatabase(fxDatabase.SQLITE, dbname = 'usdToEUR.sqlite')
dbms_usdToEUR .create_db_tables()
dbms_usdToEUR .print_all_data()

dbms_usdToGBP = fxDatabase.FXDatabase(fxDatabase.SQLITE, dbname = 'usdToGBP.sqlite')
dbms_usdToGBP .create_db_tables()
dbms_usdToGBP .print_all_data()

dbms_usdToCHF = fxDatabase.FXDatabase(fxDatabase.SQLITE, dbname = 'usdToCHF.sqlite')
dbms_usdToCHF .create_db_tables()
dbms_usdToCHF .print_all_data()

dbms_cadToUSD = fxDatabase.FXDatabase(fxDatabase.SQLITE, dbname = 'cadToUSD.sqlite')
dbms_cadToUSD .create_db_tables()
dbms_cadToUSD .print_all_data()


dbms_audToUSD = fxDatabase.FXDatabase(fxDatabase.SQLITE, dbname = 'audToUSD.sqlite')
dbms_audToUSD .create_db_tables()
dbms_audToUSD .print_all_data()


dbms_euroToUSD = fxDatabase.FXDatabase(fxDatabase.SQLITE, dbname = 'euroToUSD.sqlite')
dbms_euroToUSD .create_db_tables()
dbms_euroToUSD .print_all_data()

dbms_gbpToUSD = fxDatabase.FXDatabase(fxDatabase.SQLITE, dbname = 'gbpToUSD.sqlite')
dbms_gbpToUSD .create_db_tables()
dbms_gbpToUSD .print_all_data()

dbms_chfToUSD = fxDatabase.FXDatabase(fxDatabase.SQLITE, dbname = 'chfToUSD.sqlite')
dbms_chfToUSD .create_db_tables()
dbms_chfToUSD .print_all_data()