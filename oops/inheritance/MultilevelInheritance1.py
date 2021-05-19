class Person:
    def m1(self,name,age):
        print("inside person class")
        self.name = name
        self.age = age
        print("Person name=",self.name)
        print("age=",self.age)

class Child(Person):
    def m2(self,name,age):
        print("inside the child class")
        self.name = name
        self.age = age
        print("child name=", self.name)
        print("age=", self.age)

class Parent(Person):
    def m3(self,name,age):
        print("inside the Parent class")
        self.name = name
        self.age = age
        print("Parent name=", self.name)
        print("age=", self.age)

class Student(Child):
    def m4(self,name,age):
        print("inside the Student class")
        self.name = name
        self.age = age
        print("Person name=", self.name)
        print("age=", self.age)

obj=Student()
obj.m1("UnniKrishnan",52)
obj.m2("Ujju",15)
obj.m4("Krishnajith",24)
ob=Parent()
ob.m3("Sujatha",44)

