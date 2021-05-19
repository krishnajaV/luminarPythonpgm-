my_list=[1,0,7,5,2,3,5,7,2,0,1,10]
# my_list.sort()
# print(my_list)
# duplicate=[]
# for i in my_list:
#     if i not in duplicate:
#         duplicate.append(i)
#     else:
#         print(i)
#
my_list=[1,0,7,5,2,3,5,7,2,0,1,10]
lis=list(set(my_list))
print(lis)