# 15. Write a Python program to get the volume of a sphere with radius 6
import math
radi = float(input("Enter radius: "))
Volume = 4/3* math.pi * math.pow(radi,3)
print("Volume of sphere: ", Volume)