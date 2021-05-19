# class Student:
#     def details(self):
#         f = open("student", "r")
#         for i in f:
#             print(i)
# c=Student()
# c.details()

class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printval(self):
        print("name:",self.name)
        print("age:", self.age)
    def __str__(self):
        return self.name
f=open("student",'r')
for line in f:
    data=line.rstrip("\n").split(",")
    name=data[0]
    age=data[1]
    obj=Student(name,age)
    print(obj)
    obj.printval()


