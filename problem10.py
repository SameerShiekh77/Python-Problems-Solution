# 10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. 
# Sample value of n is 5
# Expected Result : 615

n = int(input("Enter any number: "))
n1= int("%s" % n)
n2 = int("%s%s" % (n,n))
n3 = int("%s%s%s" % (n,n,n))
print("Sample value of n is ", n)
print("Expected Result: ",n1+n2+n3)