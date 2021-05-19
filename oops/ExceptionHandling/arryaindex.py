
list=[1,2,3]
try:
    n=int(input("enter the index"))
    print(list[n])
except:
    print("index out of range")
finally:
    print("inside finally")


