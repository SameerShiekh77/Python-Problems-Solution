# 23. Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string.
# Return the n copies of the whole string if the length is less than 2. 

st = input("Enter Text: ")
n = int(input("Enter no of copies: "))
if len(st) <2:
    print(st*n)
else:
    new_st = st[0:2] *n
    print(new_st)
