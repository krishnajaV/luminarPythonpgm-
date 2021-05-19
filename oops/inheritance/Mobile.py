class Person:
    def details(self, name, id, gender):#base class,super class,parent class
        self.name = name
        self.id = id
        self.gender = gender
        print(self.name)
        print(self.id)
        print(self.gender)
class Mobile:
    def print(self):
        print("I have 1+")
class Child(Person,Mobile):
    def info(self,college,place):
        self.college = college
        self.place = place
        print(self.college)
        print(self.place)
per=Person()
per.details("Anju",25,"Female")
mob=Mobile
ch=Child()
ch.details("Anu",12,"Female")
ch.print()
ch.info("Luminar","kakkanad")