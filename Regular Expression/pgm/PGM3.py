import re
n=input("enter ")
x='([a-zA-Z]+/d$)'
i=re.finditer( x , n)
if i is not None:
    print("valid")
else:
    print("invalid")
