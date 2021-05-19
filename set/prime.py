s1={1,2,5,7,4,8,9,66,8,5,42,55}
prime=set()
non_prime=set()
for i in s1:
    if (i>0):
        for j in range(2,i):
            if(i%j==0):
                non_prime.add(i)
                break
        else:
            prime.add(i)
print(prime)
print(non_prime)


