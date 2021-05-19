# Create an Animal class using constructor and build a child class for Dog?
class Animal:
    def __init__(self, name, type):
        self.name=name
        self.type=type
        print("name=",self.name)
        print("type=",self.type)
class Dog(Animal):
    def __init__(self,leg,name,type):
        super().__init__(name,type)
        self.leg = leg

        print("legs=", self.leg)
ob=Dog(4,'puppy','mammel')
