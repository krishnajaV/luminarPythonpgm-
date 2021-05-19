import re
n="56kg"
x='\d{2}[a-z]{2}'
i=re.fullmatch( x , n)
if i is not None:
    print("valid")
else:
    print("invalid")
