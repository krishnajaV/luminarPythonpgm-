# def add(num1,num2):#parametr1,paramweter2
#     return  num1+num2
# res=add(10,20)#arg1,arg2
# print(res)
#
#
#
#
# def add_three(num1,num2,num3):
#     return num1+num2+num3


# def add(*args):
#     print(args)
# add(10)
# add(10,20)
# add(20,10,30)


def add(*args):
    res=0
    for num in args:
        res+=num
    return res
print(add(10,20,30,40))