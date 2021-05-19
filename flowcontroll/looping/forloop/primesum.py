min=int(input("enter the lowerlimit"))
max=int(input("enter the upperlimit"))
sum=0
for a in range(min,max):
    if (a>1):
        for i in range(2,a):
            if (a % i )==0:
                break
        else:
              print(a)
              sum=sum+a
print("sum of prime number is",sum)

