# Create a valid phone numbers file from the following file?
f=open("phone","r")
for i in f:
    data=i.rstrip("\n").split(",")
    phonenum=data[0]
import re
f=open("phone","r")
n=phonenum
x='[+][9][1]\d{10}'
match=re.fullmatch( x , n)
for i in f:
     if match is not None:
         print("valid:",phonenum)
     else:
         print("invalid:", phonenum)


