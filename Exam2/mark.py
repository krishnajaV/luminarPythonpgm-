class Person:
    def properties(self,name,std,dept,mark):
        self.name=name
        self.std=std
        self.dept=dept
        self.mark=mark
        print(self.name)
        print(self.std)
        print(self.dept)
        print(self.mark)
class Student(Person):
    def properties(self,name,std,dept,mark):
        self.name=name
        self.std=std
        self.dept=dept
        self.mark=mark
        print(self.name,self.std,self.dept,self.mark)
f=open("Studentdetails","r")
for i in f:
    data=i.rstrip("\n").split(",")
    name=data[0]
    std=data[1]
    dept=data[2]
    mark=data[3]
    while(max(mark)):
        c=Student()
        c.properties(name,std,dept,mark)
    break
