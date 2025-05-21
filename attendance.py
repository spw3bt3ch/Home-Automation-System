import datetime as dt
import time

time = dt.datetime.now()

print("STAFF ATTENDANCE SYSTEM(ARS)")

clock = ["Clock-In", "Clock-Out"]
for clk in enumerate(clock, start=1):
    print(f"{clk[0]}. {clk[1]}")
print()
clock = int(input("Clock-In/Clock-Out (1 or 2): "))
print()
if clock == 1:
    print(f"Welcome\nTime-In: {time}")
    print()
elif clock == 2:
    print(f"Bye!\nTime-Out: {time}")
    print()
