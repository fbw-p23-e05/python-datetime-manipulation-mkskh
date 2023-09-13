from datetime import datetime, timedelta

# Using the variable called current_datetime, add 7 days to your current day

current_datetime = datetime(2021, 7, 8)
time_plus_15days = current_datetime + timedelta(days = 7)
reformat = time_plus_15days.strftime('%Y-%m-%d')
print(reformat)
