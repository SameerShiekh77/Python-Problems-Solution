# 19. Write a Python program to get a new string from a given string where "Is" has been added to the front.
# If the given string already begins with "Is" then return the string unchanged. 

def New_String(str):
    if len(str) >=2 and str[:2] == "is":
        return str
    else:
        return "Is " + str
st = input("Enter any sentence: ")
print(New_String(st))

