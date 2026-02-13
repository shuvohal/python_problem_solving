#Current Day, Weekday, Month, Year in Python

import datetime

now = datetime.datetime.now()

day = now.day
weekday = now.strftime("%A")
month = now.month
year = now.year

print("Day:", day)
print("Weekday:", weekday)
print("Month:", month)
print("Year:", year)
