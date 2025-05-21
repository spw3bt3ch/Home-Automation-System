import sqlite3
import random
from datetime import datetime
from HASfunctions import pin_generator


connection = sqlite3.connect("residence.db")
cur = connection.cursor()

# cur.execute("""
# CREATE TABLE users (
#             first_name TEXT NOT NULL,
#             last_name TEXT NOT NULL,
#             email TEXT UNIQUE NOT NULL,
#             username TEXT UNIQUE NOT NULL,
#             password TEXT NOT NULL
#             )
# """)

# print("A new table has been created.")


pin_generator()

# cur.execute("""
# CREATE TABLE visitors (
#             Name TEXT NOT NULL,
#             Mobile_Number TEXT NOT NULL,
#             Appointment_Creator TEXT NOT NULL,
#             Pin INTEGER NOT NULL,
#             Timestamp TEXT NOT NULL
#             )
# """)

# print("Visitors Table has been created successfully")

# cur.execute("""
#             CREATE TABLE visitors_messages (
#             Visitor_Name TEXT NOT NULL, 
#             Message TEXT NOT NULL, 
#             Timestamp TEXT NOT NULL
#             )
# """)
# print("Visitors' Messages table has been created successfully")


#     cur.execute("""CREATE TABLE activities_log (
#                 Visitor_Name TEXT NOT NULL,
#                 Visitor_Login_Time TEXT NOT NULL,
#                 Username TEXT NOT NULL,
#                 Users_Login_Time TEXT NOT NULL)
# """)
#     print("Activities Log table has been created successfully")
