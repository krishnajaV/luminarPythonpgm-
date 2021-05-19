tot_student={"remya","arya","sree","krishna","aby","np"}
failed_student={"remya","np"}
pass_stud=set()
# for i in tot_student:
#     pass_student=tot_student-failed_student
# print(pass_student)
for i in tot_student:
    if  i not in failed_student:
        pass_stud.add(i)
print(pass_stud,"pass students")



