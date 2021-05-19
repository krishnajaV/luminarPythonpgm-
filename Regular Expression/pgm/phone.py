import re
n=input("enter the number")
x='[+][9][1]\d{10}'
i=re.fullmatch( x , n)
if i is not None:
    print("valid")
else:
    print("invalid")
