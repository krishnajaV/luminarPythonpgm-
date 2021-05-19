# starting letter a ending letter b
import re
n=input("enter the number")
x='(^a+b$)'
i=re.finditer( x , n)
if i is not None:
    print("valid")
else:
    print("invalid")
