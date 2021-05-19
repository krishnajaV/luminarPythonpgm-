class Student:
    def properties(self,name,std,dept,mark):
        self.name=name
        self.std=std
        self.dept=dept
        self.mark=mark
        print(self.name,self.std,self.dept,self.mark)
    def __str__(self):
        return self.name
f=open("Studentdetails","r")
list=[]
for i in f:
    data=i.rstrip("\n").split(",")
    list.append(data)
print(list)
for i in list:
    a=(int(i[3]))
    print(a)
for i in range(0,len(list)):
    for j  in range(0,len(list)-i-1):
        if list[j][-1]>list[j+1][-1]:
            temp=list[j]
            list[j]=list[j+1]
            list[j+1]=temp
print(list[-1])