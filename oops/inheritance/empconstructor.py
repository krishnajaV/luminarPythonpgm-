class Person:
    def __init__(self ,name,age,gender):
        self.name = name
        self.age = age
        self.gender=gender
        print("name=", self.name)
        print("age=", self.age)
        print("gender=", self.gender)
class Employee(Person):
    def __init__(self,empid,salary,mob,name,age,gender):
        super().__init__(name,age,gender)
        self.empid= empid
        self.salary =salary
        self.mob=mob
        print("empid=",self.empid)
        print("salary",self.salary)
        print("mobile no=", self.mob)
cr=Employee(3212,120000,"8582841245","Anu",22,"Female")
