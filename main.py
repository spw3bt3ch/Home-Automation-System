import sqlite3
import random
import datetime as dt
import time
import requests
from weather import weatherAPI
import SQLSyntax
from HASfunctions import menu
# from SQLSyntax import sqlsyntax

timestamp = dt.datetime.now()

try:
    connection = sqlite3.connect("residence.db")
    cur = connection.cursor()

    while True:
    # cur.execute("DROP TABLE users")
    # print("Table has been delete from the database")
        
        print("") 
        print("---------------------------------------------") 
        print("SMI HOME AUTOMATION SYSTEM")  
        hour = dt.datetime.now().hour
        minutes = dt.datetime.now().minute
        date = dt.datetime.now().date()
        print(f"{hour}:{minutes} GMT || {date}")
        print("")	
        
        # weatherAPI()

        print("")
        if hour >= 00 and hour < 12:
            print("Good Morning!")
        elif hour >= 12 and hour < 16:
            print("Good Afternoon!")
        elif hour >= 16 and hour < 22:
            print("Good Evening!")
        else:
            print("Hey! It's Night Time.")
        print("")	
        time.sleep(2)
        print("---------------------------------------------")
        menu()

        connection.commit()
#     # connection.close()

except KeyboardInterrupt:
    print("")
    print("\n------------------------------------")
    print("You've exited. Bye for now user!")
    print("------------------------------------")
    print("")
except requests.exceptions.ConnectionError:
    print("")
    print("\n------------------------------------")
    print("Internet Connection Error!")
    print("------------------------------------")
    print("")
except ValueError:
    print("")
    print("ERROR NOTIFICATION")
    print("\n------------------------------------")
    print("No Action Taken. Please try again!")
    print("------------------------------------")
    print("")
except requests.exceptions.ReadTimeout:
    print("")
    print("ERROR NOTIFICATION")
    print("\n------------------------------------------------")
    print("Request Time-out! (Check connection and try again)")
    print("------------------------------------------------")
    print("")