def linear():
    list3=[1,8,12,81,77,74,85,12,55]
    n=int(input("enter the number you want to search"))
    flag=0
    for i in list3:
        if (i==n):
            flag=1
    if(flag==1):
        print("number is present in list")
    else:
        print("no is not present in list")
linear()