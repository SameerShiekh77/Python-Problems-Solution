# 24. Write a Python function that takes a sequence of numbers and determines whether all the numbers are different from each other.

def sequence(ls):
    if len(ls) == len(set(ls)):
        return True
    else:
        return False

lst = [5,2,3,42,12,4,9]
print(sequence(lst)) 