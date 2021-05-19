class Person:
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
class Student(Person):
    def properties(self,name,age):
        self.name = name
        self.age = age
        print("name=", self.name)
        print("age=", self.age)


c=Student()
c.properties("krishna",12)
#METHPD OVER RIDDING IS A ONE OF  EHE PROPERTY OF POLYMORPHISM
#HERE PARENT AND CHILD HAVE SAME METHOD NAME
#CHIL OVERRIDE PARENT CLASS