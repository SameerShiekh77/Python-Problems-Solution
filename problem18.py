# 18. Write a Python program to calculate the sum of three given numbers, if the values are equal then return three times of their sum.

def Check(a, b, c):
    if a == b and b == c:
        return sum * 3
    else:
        return sum

a = int(input("Enter 1st value: "))
b = int(input("Enter 2nd value: "))
c = int(input("Enter 3rd value: "))

sum = a + b + c
print("Answer: ", Check(a, b, c))
