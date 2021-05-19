class Parent:
    def m1(self):
        print("inside parent")
class Child(Parent):
    def m2(self):
        print("inside the child class")
class Subchild(Child):
    def m3(self):
        print("inside the Subchild")

obj=Subchild()
obj.m1()
obj.m2()
obj.m3()
