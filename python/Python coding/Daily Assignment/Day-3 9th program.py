#Use the Datetime Module:
# Write a program that imports the datetime module and uses it to:
# Get and print the current date and time .
# Calculate and print the number of days between two dates.
# Format and print the current date in the format "DD-MM-YYYY"
import datetime
now=datetime.datetime.now()
print(now)
d1=datetime.date(2024,1,1)
d2=datetime.date(2024,12,31)
print("days:",(d2-d1).days)
print(now.strftime("%d-%m-%y"))
