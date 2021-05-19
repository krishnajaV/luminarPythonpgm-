# num1=int(input("enter the number1"))
# num2=int(input("enter the number2"))
# num3=int(input("enter the number3"))
# if(num1>num2)&(num1>num3):
#     if(num2>num3):
#        print(num2, " is second highest number")
#     else:
#        print(num3, " is second highest number")
# elif(num2>num1)&(num2>num3):
#     if(num1>num3):
#         print(num1, " is second highest number")
#     else:
#         print(num3, " is second highest number")
# elif(num3>num1)&(num3>num2):
#     if (num1 > num2):
#         print(num1, " is second highest number")
#     else:
#         print(num2, " is second highest number")
num1=int(input("enter the number"))
num2=int(input("enter the number"))
num3=int(input("enter the number"))
if(num1>num2)&(num1>num3):
    if(num2>num3):
        print(num2, "is second largest number")
    else:
        print(num3 ,"is second largest number")
elif(num2>num1)&(num2>num3):
    if(num1>num3):
        print(num3," id second larest number")
    else:
        print(num1 ,"is second largest number")
elif(num3>num1)&(num3>num2):
    if(num1>num2):
        print(num1, "is second largest numnber")
    else:
        print(num2, "issecond largest number")