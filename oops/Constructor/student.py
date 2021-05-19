class Student:
    def __init__(self ,name,id,school):
        self.name=name
        self.id = id
        self.school= school
    def display(self):
        print(self.name)
        print(self.id)
        print(self.school)
ob=Student("anju",1,"Luminar")
ob.display()



