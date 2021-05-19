# single inharitance
class Person:
    def details(self, name, id, gender):#base class,super class,parent class
        self.name = name
        self.id = id
        self.gender = gender
        print(self.name)
        print(self.id)
        print(self.gender)
class Student(Person):#derived class,sub class,child class
    def printval(self,dept,college):
        self.dept=dept
        self.college=college
        print(self.dept)
        print(self.college)


ob=Person()
ob.details("anju", 1, "Female")
st=Student()
st.printval("CSE","Luminar")
st.details("anu",2,"female")
