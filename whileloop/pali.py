n=int(input("enter the number"))
temp=n
pali=0
while(temp>0):
    num=temp%10
    pali=pali*10+num
    temp=temp//10
if(pali==n):
    print("number is palindrom")
else:
    print("number is not palindrom")