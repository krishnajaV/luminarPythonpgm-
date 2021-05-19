import re
n=input("enter:")
x='[K][L]\d{2}[A-Z]{2}/d{4}$'
i=re.fullmatch( x , n)
if i is not None:
    print("valid")
else:
    print("invalid")
