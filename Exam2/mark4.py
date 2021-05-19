class Student:
    def __init__(self, name, age, dept, mark):
        self.name = name
        self.age = age
        self.dept = dept
        self.mark = mark

    def printval(self):
        print("name:", self.name)
        print("age:", self.age)
        print("deptname:", self.dept)
        print("mark:", self.mark)

    def __str__(self):
        return self.name


f = open("studentdetails", 'r')
list = []
for i in f:
    data = i.rstrip("\n").split(",")
    name = data[0]
    age = data[1]
    dept = data[2]
    mark = data[3]
    obj = Student(name, age, dept, mark)
    list.append(obj)
mark = []
for j in list:
    mark.append(j.mark)
print(mark)
for j in list:
    if (j.mark == max(mark)):
        print(j.name, j.age, j.dept, j.mark)
