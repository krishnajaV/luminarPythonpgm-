# What is method overriding give an example using Books class?
#override is is one example of polymorphism
# here parent and child have same metods
# here chide override parent classs
class Employee:
    def properties(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender=gender
        print("name=", self.name)
        print("age=", self.age)
        print("gender=", self.gender)
        print("10 lack rs,2 car")
    def marry(self):
        print("with ram")
class Student(Employee):
    def properties(self,name,age):
        self.name = name
        self.age = age
        print("name=", self.name)
        print("age=", self.age)


c=Student()
c.properties("krishna",12)