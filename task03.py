from datetime import datetime, timedelta 

# Your task is to write a reminder message for a customer that is being sent out on 2020-01-01 to please pay in 25 days. Create a string that stores a message to a customer called Friedrich, print out the message to the terminal.

current_date = datetime(2020, 1, 1)
current_date += timedelta(days = 25)
reformat = current_date.strftime('%d %B, %Y')
print(f'Hello Friedrich, your rent of 300 € is due on {reformat}.')