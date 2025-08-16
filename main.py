from datetime import date
from datetime import datetime
from weather import forecast

# flow: get date > check area temps > determine if good conditions > display results
today = date.today()
print(today)

print("CragCast can forecast up to 16 days ahead. If only climbing for one day, put the same date.")
print("Put dates in form: 2025-08-11")
# handle date form or have it input correctly?
start = input("start date: ")
end = input("end date: ")
# forecast(start, end)


