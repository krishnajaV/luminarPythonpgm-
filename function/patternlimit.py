a=int(input("enter the initial range"))
n=int(input("enter the final range"))
for i in range(a,n):
    if(i%2==0):
        for j in range(1,n):
             for k in range(1,j):
                 print(i, end="")
             print()
    else:
        for x in range(n,1,-1):
            for y in range (1,x):
               print(i,end="")
            print()




