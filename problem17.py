# 17. Write a Python program to test whether a number is within 100 of 1000 or 2000.

def near_thousand(n):
      return ((abs(1000 - n) <= 100) or (abs(2000 - n) <= 100))
num = int(input("Enter any integer: "))
print(near_thousand(num))
