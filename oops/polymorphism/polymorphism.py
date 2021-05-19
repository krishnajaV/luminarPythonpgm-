#polymorphism is many form
#1.overloading=same method name,different parameter name
#* python not support overloading
#2.overriding:same method name,same parameter
#*.python support overriding
#child class method call,parent class is over ridiing
class Parent:
    def properties(self):
        print("10 lack rs,2 car")

    def marry(self):
        print("with ram")
class Child(Parent):
    def marry(self):
        print("with arun")

c=Child()
c.marry()