
try:
    a = int(input("enter the number"))
    b = int(input("enter the number"))
    sum= a+b
    print(sum)
except:
    print("please enter the integer")
finally:
    print("finally")
#in this case try and except and finally work at a time.