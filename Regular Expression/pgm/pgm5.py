#write a code for first letter should be number maximum8-15 letter


# import re
# n=input("enter:")
# x='([^0-9][a-zA-Z]\W{8,15})'
# i=re.finditer( x , n)
# if i is not None:
#     print("valid")
# else:
#     print("invalid")





import re
n=input("enter:")
x='([\D]{8,15}$)'
i=re.fullmatch( x , n)
if i is not None:
    print("valid")
else:
    print("invalid")

