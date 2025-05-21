import sqlite3
import SQLSyntax
import datetime as dt
import random

connection = sqlite3.connect("residence.db")
cur = connection.cursor()

timestamp = dt.datetime.now()

def pin_generator():
    pin = random.randint(1000, 9999)
    return pin

def users_registration():
    print("")
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    email = input("Email Address: ")
    username = input("Choose A Username: ")
    # pin = random.randint(1000, 9999) # 4 digit PIN generator
    password = input("Password: ")
    password2 = input("Confirm Password: ")
    if password2 == password:
        cur.execute(f"INSERT INTO users (first_name, last_name, email, username, password) VALUES ('{first_name}', '{last_name}', '{email}', '{username}', '{password}')")
        print("Registration completed!")
    else:
        print("Password does not match, confirm characters and try again.")
    print("")
    print("--------------------------------")
    print(f"LOGIN DETAILS\nUsername: {username}\nPassword: {password}")
    print("--------------------------------")
    print("")
    login()

    connection.commit()

def v_module():
    v_count = 0
    while True:
        print("VISITORS MENU")
        v_menu = ["Login", "Drop a message", "Home Page"]
        for sn, menu in enumerate(v_menu, start=1):
            print(f"{sn}. {menu}")
        print("")
        v_option = int(input("Choose An Option (1-3): "))
        if v_option == 1:
            while True:
                print("")
                pin = int(input("ENTER PIN: "))
                cur.execute(f"SELECT Pin FROM visitors WHERE Pin = {pin}")
                global r_pin
                v_count += 1
                r_pin = cur.fetchall()

                if r_pin:
                    cur.execute(F"SELECT Name FROM visitors WHERE Pin = {pin}")
                    global visitor_name
                    visitor_name = cur.fetchall()
                    cur.execute(f"SELECT Appointment_Creator FROM visitors WHERE Pin = {pin}")
                    creator_name = cur.fetchall()

                    cur.execute(f"INSERT INTO activities_log (Visitor_Name, Visitor_Login_Time, Username, Users_Login_Time) VALUES ('{visitor_name[0][0]}', '{timestamp}', 'Resident', '{timestamp}')")
                    connection.commit()

                    for vn, cn in zip(visitor_name, creator_name):
                        print(f"Hi {vn[0]}, {cn[0]} has been expecting you.\nYou're welcome!")
                        print("")
                        exit()
                elif v_count >= 3:
                    print("Too much Attempts!")
                    exit()
                elif len(r_pin) < 4:
                    print("Invalid PIN lenght(Too short), please try again")
                elif len(r_pin) > 4:
                    print("Invalid PIN lenght(Too long), please try again")
                else:
                    print("Invalid Login, try again or contact a resident.")
            
        elif v_option == 2:
            while True:
                visitor = input("Sender Name: ")
                print("Drop your message")
                message = input("Type Here: ")
                if message:
                    cur.execute(f"INSERT INTO visitors_messages (Visitor_Name, Message, Timestamp) VALUES ('{visitor}', '{message}', '{timestamp}')")
                    print("Message Saved!")
                    print("")
                    connection.commit()
                    break
                else:
                    print("Type your message please!")
            
        elif v_option == 3:
            break

        else:
            print("Invalid Option selected. \nPlease choose from the options provided")

def read_messages():
    print("")
    print("ALL MESSAGES")
    cur.execute("SELECT * FROM visitors_messages")
    messages = cur.fetchall()
    if messages:
        for sn, mssg in enumerate(messages, start=1):
            print(f"SN: {sn}\nNAME: {mssg[0]}\nMESSAGE: {mssg[1]}\nTIMESTAMP: {mssg[2]}")
            print("........................................")
    else:
        print("Message box is empty.")
        print("")
        
def menu():
        while True:
            main_menu = ["Resident", "Visitor", "Exit"]
            while True:
                print("MAIN MENU")
                for sn, mm in enumerate(main_menu, start=1):
                    print(f"{sn}. {mm}")
                print("")
                user_menu_option = int(input("Choose An Option(1-3): "))
                if user_menu_option == 1:
                    login()
                elif user_menu_option == 2:
                    v_module()  
                    print("") 
                elif user_menu_option == 3:
                    print("See you later.")
                    print("")
                    exit()
                    break
                else:
                    print("")
                    print("Invalid selection, please select from (1-3)")
                    print("")
def manage_visitors():
    while True:
        print("MANAGE VISITORS")
        print("")
        print("VISITORS MENU")
        visitors_menu = ["View All Visitors", "Delete Visitor", "Update Visitor", "Clear Visitors Table", "Exit"]
        for sn, vm in enumerate(visitors_menu, start=1):
            print(f"{sn}. {vm}")
        print("")
        visitors_menu_option = int(input("Choose An Option(1-5): "))    
        if visitors_menu_option == 1:
            print("")
            print("ALL VISITORS")
            cur.execute("SELECT * FROM visitors")
            table = list(cur.fetchall())
            if table:
                for sn, t in enumerate(table, start=1):
                    print(f"{sn}. {t[0]} {t[1]} {t[2]} {t[3]} {t[4]}")
                print("")
                print(f"{len(table)} visitors in total")
                print("")
            else:
                print("Table is presently empty.")
                print("")

        elif visitors_menu_option == 2:
            print("")
            print("DELETE VISITOR")
            name = input("Enter Visitor's Name to delete: ")
            cur.execute(f"DELETE FROM visitors WHERE Name = '{name}'")
            connection.commit()
            print(f"{name} has been deleted successfully.")
            print("")

        elif visitors_menu_option == 3:
            print("")
            print("UPDATE VISITOR DETAILS")
            name = input("Enter Visitor's Name to update: ")
            cur.execute(f"SELECT * FROM visitors WHERE Name = '{name}'")
            table = list(cur.fetchall())
            if table:
                for sn, t in enumerate(table, start=1):
                    print(f"{sn}. {t[0]} {t[1]} {t[2]} {t[3]} {t[4]}")
                mobile_number = input("Mobile Number: ")
                pin = input("PIN: ")
                cur.execute(f"""UPDATE visitors SET Mobile_Number='{mobile_number}', Pin='{pin}' WHERE Name='{name}'""")
                connection.commit()
                print(f"{name} has been updated successfully.")
                print("")
        elif visitors_menu_option == 4:
            cur.execute("SELECT * FROM visitors")
            v_table = cur.fetchall()
            if v_table:
                cur.execute("DELETE FROM visitors")
                print("Visitors' Table has been cleared!")
                print("")
                connection.commit()
            else:
                print("Table has no record to delete")
                print("")

        elif visitors_menu_option == 5:
            print("")
            print("You Exited!")
            break
        else:
            print("Invalid selection")

def clear_messages():
    print("")
    print("CLEAR MESSAGES")
    cur.execute("DELETE FROM visitors_messages")
    connection.commit()
    print("Messages have been cleared successfully.")
    print("")

def activities_log():
    print("")
    print("ACTIVITIES LOG")
    cur.execute("SELECT * FROM visitors_messages")
    messages = cur.fetchall()
    if messages:
        for sn, mssg in enumerate(messages, start=1):
            print(f"SN: {sn}\nNAME: {mssg[0]}\nMESSAGE: {mssg[1]}\nTIMESTAMP: {mssg[2]}")
            print("........................................")
    else:
        print("No activities log yet.")
        print("")

def download_log_file():
    print("")
    print("DOWNLOAD LOG FILE")
    cur.execute("SELECT * FROM visitors_messages")
    messages = cur.fetchall()
    filename = input("Enter file name: ")
    if messages:
        with open(f"{filename}.txt", "w") as log_file:
            for sn, mssg in enumerate(messages, start=1):
                log_file.write(f"SN: {sn}\nNAME: {mssg[0]}\nMESSAGE: {mssg[1]}\nTIMESTAMP: {mssg[2]}\n")
                log_file.write("........................................\n\n")
        print("Log file has been downloaded successfully.")
        print("")
    else:
        print("No activities log yet.")
        print("")

def activities_log():
    print("")
    activities_log = ["View Activities Log", "Download Activities Log", "Exit"]
    print("")
    for activity in enumerate(activities_log, start=1):
        print(f"{activity[0]}. {activity[1]}")
    print("")
    log_menu_option = int(input("Choose An Option(1-3): "))
    if log_menu_option == 1:
        print("")
        print("ACTIVITIES LOG")
        cur.execute("SELECT * FROM activities_log")
        activities = cur.fetchall()
        if activities:
            for sn, act in enumerate(activities, start=1):
                print(f"SN: {sn}\nVISITOR NAME: {act[0]}\nVISITOR LOGIN TIME: {act[1]}\nUSERNAME: {act[2]}\nUSER LOGIN TIME: {act[3]}")
                print("........................................")
        else:
            print("No activities log yet.")
            print("")
    elif log_menu_option == 2:
        print("")
        print("DOWNLOAD ACTIVITIES LOG")
        cur.execute("SELECT * FROM activities_log")
        activities = cur.fetchall()
        filename = input("Enter file name: ")
        if activities:
            with open(f"{filename}.txt", "w") as log_file:
                for sn, act in enumerate(activities, start=1):
                    log_file.write(f"SN: {sn}\nVISITOR NAME: {act[0]}\nVISITOR LOGIN TIME: {act[1]}\nUSERNAME: {act[2]}\nUSER LOGIN TIME: {act[3]}\n")
                    log_file.write("........................................\n\n")
            print("Log file has been downloaded successfully.")
            print("")
    else:
        print("No activities log yet.")
        print("")

def private_access():
    while True:
        print("")
        print("PRIVATE ACCESS")
        private_menu = ["Manage Users", "Manage Visitor", "History Log", "Download Messages (.txt file)", "Read & Download Logs", "Clear Messages", "Exit"]
        for menu in enumerate(private_menu, start=1):
            print(f"{menu[0]}. {menu[1]}")
        print("")
        private_menu_option = int(input("Choose An Option(1-7): "))
        if private_menu_option == 1:
            print("")
            print("MANAGE USERS")
            while True:
                print("")
                print("USER MANAGEMENT MENU")
                user_management_menu = ["Add User", "Delete User", "Update User", "Exit"]
                for sn, umm in enumerate(user_management_menu, start=1):
                    print(f"{sn}. {umm}")
                print("")
                user_management_option = int(input("Choose An Option(1-4): "))
                if user_management_option == 1:
                    users_registration()
                elif user_management_option == 2:
                    print("")
                    print("DELETE USER")
                    username = input("Enter Username to delete: ")
                    cur.execute(f"DELETE FROM users WHERE username = '{username}'")
                    connection.commit()
                    print(f"{username} has been deleted successfully.")
                    print("")

                elif user_management_option == 3:
                    print("")
                    print("UPDATE USER DETAILS")
                    username = input("Enter Username to update: ")
                    cur.execute(f"SELECT * FROM users WHERE username = '{username}'")
                    table = list(cur.fetchall())
                    if table:
                        for sn, t in enumerate(table, start=1):
                            print(f"{sn}. {t[0]} {t[1]} {t[2]} {t[3]} {t[4]}")
                        first_name = input("First Name: ")
                        last_name = input("Last Name: ")
                        email = input("Email Address: ")
                        password = input("Password: ")
                        cur.execute(f"""UPDATE users SET first_name='{first_name}', last_name='{last_name}', email='{email}', password='{password}' WHERE username='{username}'""")
                        connection.commit()
                        print(f"{username} has been updated successfully.")
                        print("")

                elif user_management_option == 4:
                    break
                else:
                    print("Invalid selection")

        elif private_menu_option == 2:
            manage_visitors()
        elif private_menu_option == 3:
            activities_log()
        elif private_menu_option == 4:
            download_log_file()
        elif private_menu_option == 5:
            activities_log()
        elif private_menu_option == 6:
            clear_messages()
        elif private_menu_option == 7:
            print("")
            print("You Exited!")
            break
        else:
            print("Invalid selection")

def full_menu():
        main_menu = ["Check messages", "Register a new User", "View All Users", "Check Camera footages", "Generate a visitors PIN", "PRIVATE ACCESS", "Home Page"]
        print("MAIN MENU")
        while True:
            for sn, mm in enumerate(main_menu, start=1):
                print(f"{sn}. {mm}")
            print("")
            user_menu_option = int(input("Choose An Option(1-7): "))
            if user_menu_option == 1:
                read_messages()
                print("")
            elif user_menu_option == 2:
                users_registration()
            elif user_menu_option == 3:
                view_users()
            elif user_menu_option == 4:
                print("Security module not yet available, please check back later or update software.")
                print("")
            elif user_menu_option == 5:
                visitor_pin()
            elif user_menu_option == 6:
                private_access()
            elif user_menu_option == 7:
                print("You Exited!")
                print("")
                break
            else:
                print("Invalid selection")

def view_users():
    print("")
    print("---------------------------------------------------------")
    print("ALL APP USERS")
    cur.execute("SELECT * FROM users")
    table = list(cur.fetchall())
    if table:
        for sn, t in enumerate(table, start=1):
            print(f"{sn}. {t[0]} {t[1]} {t[2]}")
        print("---------------------------------------------------------")    
        print(f"{len(table)} users in total")
        print("---------------------------------------------------------")
        print("")
    else:
        print("Table is presently empty.")
        print("")


# Login Function
def login():
    global r_count
    r_count = 0
    while True:
        print("")
        print("RESIDENT LOGIN")
        username = input("Username: ")
        password = input("Password: ")
        r_count += 1
        print("")
        # Below is a reference to the login details
        cur.execute(f"SELECT username, password FROM users WHERE username = '{username}' AND password = '{password}'")
        login_details = cur.fetchall()
        
        if r_count > 3:
                print("Too much Attempts!")
                exit()

        if login_details:
            print("")
            # Below is a reference to the first name of the user
            cur.execute(f"SELECT first_name FROM users WHERE username = '{username}' AND password = '{password}'")
            global cu
            chief_user = cur.fetchone()
            for cu in chief_user:
                print(f"Hi {cu}, you're welcome")
            print("")
            print("USER MAIN MENU")
            full_menu()
            break
        else:
            print("Invalid Username or Password, please try again")
            continue

def visitor_pin():
    print("VISITOR's APPOINTMENT")
    name = input("Visitor's Fullname: ")
    mobile_number = input("Mobile Number: ")
    pin = pin_generator()
    time = dt.datetime.now()
    created_by = cu

    cur.execute(f"""
                INSERT INTO visitors (Name, Mobile_Number, Appointment_Creator, Pin, Timestamp) 
                VALUES ('{name}', '{mobile_number}', '{created_by}', {pin}, '{time}')
                """)
    
    connection.commit()

    print("")
    print("STATUS MESSAGE")
    print(f"{name} appointment as a visitor has been created successfully\nDATE & TIME CREATED: {time}")
    print("----------------------------------------------------")
    print(f"{name.upper()} ACCESS DETAILS:\nUsername: {name.split()[0]}\nAutogenerated PIN: {pin}\n")
    print("----------------------------------------------------")
    print("")
    print(f"Program has sent Access Details to {name} on your behave.")
    print("")