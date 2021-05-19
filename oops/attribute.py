class Person:
    def details(self,name,age):
        self.name=name
        self.age=age
    def printval(self):
        print(self.name)
        print(self.age)
ob=Person()
ob.details("anju",25)
ob.printval()