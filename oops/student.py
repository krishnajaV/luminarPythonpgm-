#instance variable related to method,self keyword used call instance variable
#class variable related to class,class name used call
class Student:
    collegec="Luminar"
    def setval(self, name,id):
        self.name=name
        self.id=id
    def display(self):
        print("name=",self.name)
        print("id=", self.id)
        print("college=", Student.college)
st=Student()
st.setval("Arya",4)
st.display()
st2=Student()
st2.setval("Krishna",3)
st2.display()