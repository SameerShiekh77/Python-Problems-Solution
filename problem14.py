# 14. Write a Python program to calculate number of days between two dates.
# Sample dates : (2014, 7, 2), (2014, 7, 11)
# Expected output : 9 days

import datetime

date1 = (2014,7,2)
date2 = (2014,7,11)

f_date = datetime.date(date1[0],date1[1],date1[2])
l_date = datetime.date(date2[0],date2[1],date2[2])
print((l_date-f_date).days)