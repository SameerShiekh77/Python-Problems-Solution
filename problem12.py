# 12. Write a Python program to print the calendar of a given month and year.
# Note : Use 'calendar' module.

import calendar
month = int(input("Enter month number: "))
year = int(input("Enter year number: "))
print(calendar.month(year,month))