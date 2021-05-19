class Person:
   def details(self, name, id, gender):#base class,super class,parent class
        self.name = name
        self.id = id
        self.gender = gender
        print(self.name)
        print(self.id)
        print(self.gender)
class Employee(Person):#derived class,sub class,child class
    def printval(self,dept,age,salary):
        self.dept=dept
        self.age=age
        self.salary=salary
        print(self.dept)
        print(self.age)
        print(self.salary)


ob=Person()
ob.details("anju", 1, "Female")
em=Employee()
em.printval("CSE",25,20000)
em.details("anu",2,"female")
