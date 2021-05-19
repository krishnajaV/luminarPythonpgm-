# Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'?

import re
n=input("enter :")
x='(^a[a-zA-Z0-9\W]*b$)'
i=re.fullmatch( x , n)
if i is not None:
    print("valid")
else:
    print("invalid")
