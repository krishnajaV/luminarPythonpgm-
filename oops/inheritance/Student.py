class Student:
    def __init__(self ,stdname,rollno,age,dept):
        self.stdname = stdname
        self.rollno=rollno
        self.age = age
        self.dept=dept
        print("name=", self.stdname)
        print("rollno=", self.rollno)
        print("age=", self.age)
        print("dept=", self.dept)
    def __str__(self):
        return self.stdname+str(self.rollno)
ob=Student("anu",25,15,"cs")
print(ob)