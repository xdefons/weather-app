#ioebweathermap.org
import os  #import bilbioteki, wszystkiego
from services.log import logs, logs_read
from services.excel_file import save_to_excel
from services.mongodb import save_to_mongo
from datetime import datetime
#from os import environ  #import tylko czesci, co potencjalnie utrudnia dostep do innych,
#dzieki temu mozna by zamiast os.environ.get pisac po prostu environ.get
from config import Config

#import pymongo zeby sie zgrac z MongoDB
import pymongo

from dotenv import load_dotenv  #import czesci bilbioteki
from services.fetch_weather import fetch_weather

CITY = input("Podaj nazwę miasta: ")
print("1. Zapisuj do pliku Excel.")
print("2. Zapisuj do MongoDB.")
print("3.Zapisuj do MongoDB i pliku Excel.")
OPERATION = int(input("Wybierz rodzaj operacji:"))
weather = fetch_weather(Config.API_KEY,CITY)

match OPERATION:
    case 1:
        save_to_excel(Config.EXCEL_FILENAME, weather)
    case 2:
        save_to_mongo(weather)
    case 3:
        save_to_excel(Config.EXCEL_FILENAME, weather)
        save_to_mongo(weather)
    case _:
        print("Dane zostały dodane.")

load_dotenv() #pozwala zciagnac dane z .env i wczytac hasla, klucze API
API_KEY = Config.API_KEY


# save_to_excel("pogoda.xlsx", weather)
# save_to_mongo(weather)


logs()
#logs_read()

# while True:
#     try:
#         start()
#         print("cos działa")
#     except Exception as e:
#         print(e)
#     time.sleep(10)
