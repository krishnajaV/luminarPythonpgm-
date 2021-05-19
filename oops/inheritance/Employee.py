class Employee():
    def detals(self,empid,salary,mob,name,age,gender):
        self.empid= empid
        self.salary =salary
        self.mob=mob
        self.name = name
        self.age = age
        self.gender = gender
        print("empid=",self.empid)
        print("salary",self.salary)
        print("mobile no=", self.mob)
        print("name=", self.name)
        print("age=", self.age)
        print("gender=", self.gender)
    def __str__(self): #print to object we are using 2 string method
        return self.name
ob=Employee(101,10000,"9045231286","Krishna",24,"female")
print(ob)
