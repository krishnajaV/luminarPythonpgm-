# import re
# n=input("enter:")
# x='([a-zA-Z0-9]+[@][a-zA-Z0-9]+[.][a-z])'
# i=re.finditer( x , n )
# if i is not None:
#     print("valid")
# else:
#     print("invalid")

import re
n=input("enter:")
x='([a-zA-Z0-9]+[@][a-zA-Z-9]+[.][a-z])'
i=re.finditer( x , n )
if  i is not None:
    print("valid")
else:
    print("invalid")
