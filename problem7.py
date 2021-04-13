# 7. Write a Python program to accept a filename from the user and print the extension of that.
# Sample filename : abc.java
# Output : java

filename = input("Enter Filename with extension: ")
extension = filename.split(".")
print("Output: ", extension[-1])