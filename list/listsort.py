mylist=[1,2,5,8,41,10,12,13]
print(mylist)
newlist=[]
while mylist:
    min=mylist[0]
    for i in mylist:
        if i<min:
            min=i
    newlist.append(min)
    mylist.remove(min)
print(newlist)