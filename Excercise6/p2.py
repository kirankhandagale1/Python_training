# Write a Python program to read last n lines of a file.
import sys
f=open("k1","r")
x=f.readlines()[-1]                    
print(x)
