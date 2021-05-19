# Write a Python program to find the sequences of one upper case letter followed by lower case letters?
import re
n=input("enter :")
x='[A-Z]+[a-z]$'
i=re.fullmatch( x , n)
if i is not None:
    print("valid")
else:
    print("invalid")