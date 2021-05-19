class Person:
    def __init__(self ,name,age):
        self.name = name
        self.age = age
        print("name=", self.name)
        print("age=", self.age)
class Student(Person):
    def __init__(self,mark,rollno,name,age):
        super().__init__(name,age)
        self.mark = mark
        self.rollno =rollno
        print("mark=",self.mark)
        print("rollno",self.rollno)
cr=Student(32,12,"anu",22)
