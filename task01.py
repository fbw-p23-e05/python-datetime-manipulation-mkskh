from datetime import datetime, timedelta

# Using the variable called current_datetime, subtract 15 days from the current time.

current_datetime = datetime(2021, 7, 8)
time_minus_15days = current_datetime - timedelta(days = 15)
reformat = time_minus_15days.strftime('%Y-%m-%d')
print(reformat)
