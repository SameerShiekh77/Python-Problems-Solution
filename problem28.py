# 28. Write a Python program to count the number of characters (character frequency) in a string

sample_String = "python.org"
count = 0
result = {}
for i in sample_String:
    keys = result.keys()
    if i in keys:
        result[i] += 1
    else:
        result[i] = 1
print(result)

