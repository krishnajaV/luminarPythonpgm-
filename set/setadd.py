num=int(input("enter the limit"))
s=set()
for i in range(1,num):
    element=input("enter the element you want to add")
    s.add(element)# set not support duplicate elements
print(s)


