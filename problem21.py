# 21. Write a Python program to find whether a given number (accept from the user) is even or odd, print out an appropriate message to the user.

n = int(input("Enter a number: "))
if n %2 == 0:
    print("Even Number")
else:
    print("Odd Number")