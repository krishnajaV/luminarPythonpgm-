

def add(num1,num2):
     return  num1+num2
def sub(num1,num2):
    return num1-num2
def mul(num1,num2):
    return num1*num2
def div(num1,num2):
    return num1/num2

print("select OPeractor")
print("1.add")
print("2.substraction")
print("3.multiplication")
print("4.division")
while True:
    choice=input("enter the choice")
    if choice in("1","2","3","4"):
        x = int(input("enter the num1"))
        y = int(input("enter the num2"))
        if choice =="1":
            print(add(x,y))
        elif(choice=="2"):
            print(sub(x,y))
        elif(choice=="3"):
            print(mul(x,y))
        elif(choice=="4"):
            print(div(x,y))
        break
    else:
        print("invalid")



# if (a=="+"):
#     add()
#     break
# elif(a=="-"):
#     sep()
#     break
# elif(a=="/"):
#     div()
#     break
# elif(a==*):
#     mul()
#     break
# else
#     print("invalid")
