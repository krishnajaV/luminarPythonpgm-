count={}
f=open("exam.txt","r")
for i in f:
    words=i.split(" ")
    for i in words:
        if i not in count:
            count.update({i:1})
        else:
            val=int(count[i])
            val+=1
            count.update({i:val})
print(count)