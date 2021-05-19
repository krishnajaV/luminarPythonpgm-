class Student:
    def details(self, name, id, gender):#base class,super class,parent class
        self.name = name
        self.id = id
        self.gender = gender
        print(self.name)
        print(self.id)
        print(self.gender)
class Faculty:
    def print(self,name,sub):
        self.name= name
        self.sub = sub
        print(self.name)
        print(self.sub)
class Department(Student,Faculty):
    def info(self,deptname,college,place):
        self.deptname = deptname
        self.college = college
        self.place = place
        print(self.college)
        print(self.place)
st=Student()
#st.details("Anju",25,"Female")
fc=Faculty()
##fc.print("Anjali","Graph theory")
dp=Department()
dp.details("Anu",12,"Female")
dp.print("Happy","Dbms")
dp.info("cs","Ammini college","kakkanad")