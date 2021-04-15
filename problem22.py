# 22. Write a Python program to count the number 4 in a given list

lst = [1,4,6,7,4]
count = 0
for i in range(5):
    if 4 == lst[i]:
        count = count + 1
print("The number 4 in %d times"%count)