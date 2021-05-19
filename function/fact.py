n=int(input("enter the number"))
i=1
fact=1
if n<0:
    print("sorry negative number")
elif n==0:
    print("factorial is= 1")
else:
    for i in range(1,n+1):
        fact=fact*i
    print("factorial is =",fact)


