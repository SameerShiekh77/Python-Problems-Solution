# 29. Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, 
# return instead of the empty string.
# Sample String : 'python'
# Expected Result : 'pyon'

text = input("Enter any string: ")
if len(text) <=2:
    print("Empty String")
else:
    f_letter = text[0:2]
    l_letter = text[len(text)-2:]
    print(f_letter + l_letter)