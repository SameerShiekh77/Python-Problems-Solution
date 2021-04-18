# 30.  Write a Python program to get a string from a given string where all occurrences of its first char
# have been changed to '$', except the first char itself.
# Sample String : 'restart'
# Expected Result : 'resta$t'

text = 'restart'
char = text[0]
text = char + text[1:].replace(char,"$")
print(text)
