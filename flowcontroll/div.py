# a=int(input("enter the number"))
# b=int(input("enter the number"))
# div= a/b
# print(div)
# #here occur some error due to division by zero
# #here  we use exception handling
# here we try and except stastement
a=int(input("enter the number"))
b=int(input("enter the number"))
try:
    div= a/b
    print(div)
except:
    print("exception occured")
