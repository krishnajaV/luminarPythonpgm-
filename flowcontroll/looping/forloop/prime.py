n=int(input("enter the number"))
flag=0
for i in range(2,n,1):
 if(n%i==0):
     flag=1

if(flag>0):
    print("number is not prime")
else:
    print("number is prime")