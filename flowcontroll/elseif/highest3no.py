num1=int(input("enter the number1"))
num2=int(input("enter the number2"))
num3=int(input("enter the number3"))
if(num1>num2)&(num1>num3):
    print(num1, " is highest number")
elif(num2>num1)&(num2>num3):
    print(num2 ," is highest number")
else:
    print(num3, "is highest number")