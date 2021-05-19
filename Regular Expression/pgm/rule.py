import re
n="hello3@"
x='\w*'# check starting letter a
i=re.fullmatch( x , n)
if i is not None:
    print("valid")
else:
    print("invalid")
