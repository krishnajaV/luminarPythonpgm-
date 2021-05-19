n=int(input("enter the number"))
am=0
temp=n
while(temp>0):
    num=temp%10
    am=am+num**3  #am+(num*num*num)
    temp=temp//10
if(am==n):
    print("number is amstrong")
else:
    print("number is not amstrong")

