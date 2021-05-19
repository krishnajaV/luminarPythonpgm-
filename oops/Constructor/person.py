
#constructor:to initilize instant variable
#constructor automatically creating object

class Person:
    def __init__(self ,name,id,gender):
        self.name=name
        self.id = id
        self.gender= gender
    def display(self):
        print(self.name)
        print(self.id)
        print(self.gender)
ob=Person("anju",1,"Female")
ob.display()
