class Employee:
    def __init__(self ,name,age,gender):
        self.name = name
        self.age = age
        self.gender=gender
        print("name=", self.name)
        print("age=", self.age)
        print("gender=", self.gender)
    def __str__(self):
        return self.name+str(self.age)
ob=Employee("anu",25,"female")
print(ob)
