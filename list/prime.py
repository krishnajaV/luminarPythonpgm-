list=[2,3,4,5,6,7,8,9]
prime=[]
non_prime=[]
for i in list:
    if (i>0):
        for j in range(2,i):
            if(i%j==0):
                non_prime.append(i)
                break
        else:
            prime.append(i)
print("prime number",prime)
print("nonprime ",non_prime)

