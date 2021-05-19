class Employee():
    company_name="TCS"
    def details(self,empid,name,age,dept,salary):
        self.empid=empid
        self.name=name
        self.age=age
        self.dept=dept
        self.salary=salary
    def display(self):
        print(self.empid)
        print(self.name)
        print(self.age)
        print(self.dept)
        print(self.salary)
        print(Employee.company_name)
ob=Employee()
ob.details(1,"Arya",24,"CSE",100000)
ob.display()
ob1=Employee()
ob1.details(2,"Krishna",24,"CSE",100000)
ob1.display()
