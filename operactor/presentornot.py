# dict={ 'name':'zara','age':'18','class':'2'}
# key=input("enter the key")
# flag=0
# for i in dict:
#     if (dict[i]==key):
#         flag=1
# if(flag>0):
#         print("present")
# else:
#     print("not present")



dict={ 'name':'zara','age':'18','class':'2'}
def present(x):
    if x in dict:
        print("present")
    else:
        print(" not present")
present(5)
