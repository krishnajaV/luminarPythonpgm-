def recr_fib(n):
    if n<=1:
        return n
    else:
        return recr_fib(n-1)+recr_fib(n-2)
nterms=10
if nterms<=0:
    print("enter the limit")
else:
    print("fibnocii series")
    for i in range(nterms):
        print(recr_fib(i))

