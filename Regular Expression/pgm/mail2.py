import re
n=input("enter:")
x='[a-zA-Z0-9+-]@[a-zA-Z0-9]+\.[a-ZA-Z0-9]'
i=re.fullmatch( x , n)
if i is not None:
    print("valid")
else:
    print("invalid")
