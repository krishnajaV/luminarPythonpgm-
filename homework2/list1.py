li=[7,8,9,4,3,2,1]
# l2=[]
# for i in li:
#    # print(i)
#     if (i<=5):
#         i=i-1
#         l2.append(i)
#     else:
#        i=i+1
#        l2.append(i)
# print(l2)
op=list(map(lambda num:num+1 if num>5 else num-1,li))
print(op)
even=list(filter(lambda num:num%2==0,li))
print(even)