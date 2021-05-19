a=input("enter the string")
b="@#%^&*()';/?><.,"
no_pu=""
for i in a:
    if i not in b:
        no_pu=no_pu+i
print(no_pu)

