
a="luminar"
str=input("enter the string")
flag=0
for val in a:
    if val in str:
        flag=1
if(flag>0):
    print("present")
else:
    print(" not present")


