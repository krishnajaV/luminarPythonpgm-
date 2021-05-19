n=int(input("enter the limit"))
flag=0
for i in range(2,n):
    if(n%i==0):
        flag=1
    if(flag>0):
        print("non prime no",i)
    else:
        print("prime no is ",i)