salary_list=[(1,"anu",28,20000),(2,"vinu",23,525000),(3,"ram",25,10000)]
# for i in salary_list:
#          print(i[3])
#          mx=int(max(i[3]))
#          print(mx)
for i in range(0,len(salary_list)):
    for j in range(0,len(salary_list)-i-1):
        if(salary_list[j][-1]>salary_list[j+1][-1]):
            temp=salary_list[j]
            salary_list[j]=salary_list[j+1]
            salary_list[j+1]=temp
print("the detail of employeee highest salary is",salary_list[-1])
